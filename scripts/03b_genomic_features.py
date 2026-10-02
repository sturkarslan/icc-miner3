#!/usr/bin/env python
"""Step 03 (genomics part, ICC): binary genomic feature matrix for MINER3 causal inference (step 05).

One matrix, features x network samples: 1 = altered, 0 = profiled and not altered, empty = not profiled.
MINER's causalNetworkAnalysis() treats every non-1 column as wild type, so step 05 runs each feature
on its profiled (non-empty) samples only.

TCGA-CHOL adds gene and pathway mutations only (Xena GDC MAF); GSE107943 has no genomics (all empty).
FU-iCCA sources (paper supplementary tables):
  gene mutation     Table S1B WES calls, protein-altering classes (genomics.mutation_classes), curated
                    iCCA driver genes only (genomics.driver_genes); profiled = clinical WES_seq == Yes
  pathway mutation  OR of member gene mutations
  fusion            Table S1H RNA-seq fusion calls (FGFR2 on either side); profiled = RNA_seq == Yes
  arm-level CNA     Table S2B gene-level log2 copy ratio (no segments are published): an arm is gained /
                    lost when the median over its genes is >= / <= genomics.arm_threshold
  focal amp / HD    Table S2B ratio of the named genes >= focal_amp_threshold / <= focal_del_threshold
                    (the authors' GISTIC high-level thresholds)

A feature is kept when altered in >= min_altered samples and >= min_freq of its profiled samples.

Outputs (results/03_genomics_clinical/):
  genomic_features.csv        features x samples (1/0/empty)
  genomic_features_info.tsv   per feature: type, profiled / altered / frequency (per cohort and total), kept
  arm_cna_median_ratio.tsv    arm x sample median log2 ratio (for threshold checks)
  qc/g1_feature_frequency.png
"""

import argparse
import os
import re

import numpy as np
import pandas as pd

from hcc_common import load_params, p, setup_logging

OUT = "03_genomics_clinical"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--params", default=None)
    args = ap.parse_args()
    P = load_params(args.params)
    G = P["genomics"]
    res = p(P["paths"]["results"])
    outdir = os.path.join(res, OUT)
    os.makedirs(os.path.join(outdir, "qc"), exist_ok=True)
    log = setup_logging(outdir, "03b_genomic_features")
    cohort = "FU_iCCA"
    pre = P["cohorts"][cohort].get("sample_prefix", "")
    samples = pd.read_csv(os.path.join(res, "01_harmonized", "samples.tsv"), sep="\t")
    fu = samples.loc[samples["cohort"] == cohort, "sample"].tolist()
    net = samples["sample"].tolist()                 # all network samples; cohorts without data stay empty
    tcga = samples.loc[samples["cohort"] == "TCGA", "sample"].tolist()

    C = P["clinical"][cohort]
    clin = pd.read_csv(p(C["table"]), sep="\t", skiprows=C.get("skiprows", 0), dtype=str)
    clin.index = pre + clin[C["id_column"]].str.strip()
    wes = [s for s in fu if clin[G["wes_flag_column"]].get(s) == "Yes"]
    rna = [s for s in fu if clin[G["rna_flag_column"]].get(s) == "Yes"]

    rows, types = {}, {}

    def add(name, kind, altered, profiled):
        v = pd.Series(np.nan, index=net)
        v[profiled] = 0.0
        v[[s for s in altered if s in set(profiled)]] = 1.0
        rows[name], types[name] = v, kind

    # ---- mutations
    m = pd.read_csv(p(G["mutations"]), sep="\t", skiprows=1, dtype=str).dropna(axis=1, how="all")
    m["sample"] = pre + m["Sample_ID"].str.strip()
    m["cls"] = m["Mutation_Type"].str.split("&").str[0]
    log.info("Mutations: %d calls in %d samples (%d in network with WES flag %d); classes: %s", len(m), m["sample"].nunique(),
             len(set(m["sample"]) & set(net)), len(wes), m["cls"].value_counts().head(8).to_dict())
    wes = [s for s in wes if s in set(m["sample"])] if len(set(wes) - set(m["sample"])) > 20 else wes
    mk = m[m["cls"].isin(G["mutation_classes"])]
    by_gene = mk.groupby("Gene")["sample"].apply(set)
    # TCGA-CHOL (Xena GDC MAF): same protein-altering classes (first VEP term); sequenced = samples in the MAF
    if tcga and G.get("TCGA", {}).get("maf"):
        t = pd.read_csv(p(G["TCGA"]["maf"]), sep="\t", dtype=str)
        seq = [s for s in tcga if s in set(t["sample"])]
        tk = t[t["effect"].str.split(";").str[0].isin(G["mutation_classes"]) & t["sample"].isin(seq)]
        log.info("TCGA: %d of %d network samples in the MAF; %d protein-altering calls", len(seq), len(tcga), len(tk))
        by_gene = by_gene.combine(tk.groupby("gene")["sample"].apply(set), lambda a, b: (a if isinstance(a, set) else set())
                                  | (b if isinstance(b, set) else set()), fill_value=set())
        wes = wes + seq
    for g in G["driver_genes"]:
        add(f"MUT_{g}", "gene_mutation", by_gene.get(g, set()), wes)
    for pw, genes in G["pathways"].items():
        add(f"PATH_{pw}", "pathway_mutation", set().union(*[by_gene.get(g, set()) for g in genes]), wes)

    # ---- fusions
    f = pd.read_csv(p(G["fusions"]), sep="\t", skiprows=1, dtype=str)
    f["sample"] = pre + f["Sample_ID"].str.strip()
    for g in G["fusion_genes"]:
        add(f"FUS_{g}", "fusion", set(f.loc[(f["LeftGene"] == g) | (f["RightGene"] == g), "sample"]), rna)

    # ---- copy number (gene-level log2 ratio)
    cn = pd.read_csv(p(G["cna_gene"]), sep="\t", skiprows=1, low_memory=False).dropna(axis=1, how="all")
    cn["gene"] = cn["Gene Symbol"].astype(str).str.split("|").str[0]
    cyto = cn["Cytoband"].astype(str)
    cn["arm"] = cyto.str.extract(r"^(\d+|X|Y)([pq])").apply(lambda r: f"{r[0]}{r[1]}" if isinstance(r[0], str) else np.nan, axis=1)
    scols = [c for c in cn.columns if re.fullmatch(r"\d+", str(c).strip())]
    R = cn[scols].apply(pd.to_numeric, errors="coerce")
    R.columns = [pre + str(c).strip() for c in scols]
    cna = [s for s in fu if s in R.columns]
    log.info("Copy number: %d genes x %d samples (%d in network); %d arms", len(R), R.shape[1], len(cna), cn["arm"].nunique())
    n_arm = cn.groupby("arm").size()
    arms = [a for a in n_arm.index if n_arm[a] >= G["arm_min_genes"] and a not in G["exclude_arms"]]
    A = R.groupby(cn["arm"]).median().loc[arms, cna]
    A.to_csv(os.path.join(outdir, "arm_cna_median_ratio.tsv"), sep="\t", float_format="%.3f")
    thr = G["arm_threshold"]
    for a in sorted(arms, key=lambda x: (int(re.match(r"\d+", x).group()) if x[0].isdigit() else 99, x[-1])):
        add(f"ARM_{a}_gain", "arm_cna", A.columns[A.loc[a] >= thr], cna)
        add(f"ARM_{a}_loss", "arm_cna", A.columns[A.loc[a] <= -thr], cna)
    Rg = R.groupby(cn["gene"]).mean()
    for name, spec in G["focal"].items():
        genes = [g for g in spec["genes"] if g in Rg.index]
        if not genes:
            log.warning("focal %s: genes %s not in the copy-number table", name, spec["genes"])
            continue
        x = Rg.loc[genes, cna]
        alt = x.columns[(x >= G["focal_amp_threshold"]).any()] if spec["type"] == "amp" else x.columns[(x <= G["focal_del_threshold"]).any()]
        add(f"{'AMP' if spec['type'] == 'amp' else 'HD'}_{name}", "focal_cna", alt, cna)

    F = pd.DataFrame(rows).T
    info = pd.DataFrame({"type": pd.Series(types)})
    for c in samples["cohort"].unique():
        k = samples.loc[samples["cohort"] == c, "sample"]
        info[f"profiled_{c}"], info[f"altered_{c}"] = F[k].notna().sum(1), (F[k] == 1).sum(1)
        info[f"freq_{c}"] = (info[f"altered_{c}"] / info[f"profiled_{c}"]).round(3)
    info["profiled"], info["altered"] = F.notna().sum(1), (F == 1).sum(1)
    info["freq"] = (info["altered"] / info["profiled"]).round(3)
    info["kept"] = (info["altered"] >= G["min_altered"]) & (info["freq"] >= G["min_freq"])
    info = info.sort_values(["kept", "altered"], ascending=False)
    info.index.name = "feature"
    info.to_csv(os.path.join(outdir, "genomic_features_info.tsv"), sep="\t")
    K = F.loc[info.index[info["kept"]]]
    K.index.name = "feature"
    K.to_csv(os.path.join(outdir, "genomic_features.csv"), float_format="%.0f")
    log.info("Features kept: %d of %d -> %s", len(K), len(F), info[info["kept"]]["type"].value_counts().to_dict())
    log.info("Kept non-arm features:\n%s", info[info["kept"] & (info["type"] != "arm_cna")][["type", "profiled", "altered", "freq"] + [c for c in info.columns if c.startswith("altered_")]].to_string())
    log.info("Kept arm features:\n%s", info[info["kept"] & (info["type"] == "arm_cna")][["altered", "freq"]].T.to_string())
    log.info("Driver genes below threshold: %s", info[~info["kept"] & (info["type"] == "gene_mutation")]["altered"].to_dict())

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    k = info[info["kept"]].sort_values("freq")
    col = {"gene_mutation": "#2a78d6", "pathway_mutation": "#1baf7a", "fusion": "#eda100", "arm_cna": "#898781", "focal_cna": "#e85d2f"}
    fig, ax = plt.subplots(figsize=(5, 0.13 * len(k) + 1), layout="constrained")
    ax.barh(range(len(k)), k["freq"], color=[col[t] for t in k["type"]])
    ax.set_yticks(range(len(k)))
    ax.set_yticklabels(k.index, fontsize=5)
    ax.set_xlabel("fraction of profiled tumours altered")
    ax.margins(y=0.01)
    fig.savefig(os.path.join(outdir, "qc", "g1_feature_frequency.png"), dpi=170)


if __name__ == "__main__":
    main()
