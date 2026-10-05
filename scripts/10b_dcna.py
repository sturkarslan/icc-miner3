#!/usr/bin/env python
"""Step 10b (ICC): drug-constrained network activity (DCNA), as in the GBM / HCC work, with a causal-flow extension.

  1. Regulon activity per tumour: MINER trinary activity (-1 / 0 / +1). Discovery (374): MINER's own over - under
     membership; other cohorts: generateRegulonActivity on within-cohort gene z-scores.
  2. Drug -> regulons, two parts (docs/trial_emulation_design.md):
       target part: regulons whose regulator is a drug target or that contain a target (Open Targets, data/reference/
                    ot_drug_targets.tsv); DCNA_target = mean activity.
       causal part: when a target is an altered driver in the network (target_features below: FGFR2 -> FGFR2 fusion,
                    IDH1 -> IDH1 mutation, ERBB2 -> ERBB2 amplification, BRAF -> BRAF mutation), the regulons of its
                    causal flows (high-confidence; else MINER-filtered flows with |d| >= 0.5), each signed by the direction
                    of the regulon in altered tumours: DCNA_causal = mean of sign(d) x activity ("looks like an altered
                    tumour").
     DCNA = mean over the union (causal regulons signed). Reported separately and combined.
  3. Inhibitors predicted responsive when DCNA > 0. Combinations: independent drug action (max over drugs).
Tests: GSE255058 (FOLFOX-HAIC + lenvatinib + anti-PD-1; 9 responders / 9 non-responders): AUC per drug and for the
combination. Discovery subgroups: FGFR-inhibitor DCNA in FGFR2-fusion vs other tumours, ivosidenib DCNA in IDH1-mutant,
zanidatamab in ERBB2-amplified, anti-PD-(L)1 DCNA in STIM inflamed (immune classical + inflammatory stroma) vs others.
Outputs: results/10_response/dcna/{drug_regulons.tsv, dcna_<cohort>.tsv (+ _target / _causal), dcna_tests.tsv, subgroups.tsv}
"""

import json
import os

import numpy as np
import pandas as pd
from scipy import stats

from hcc_common import load_params, miner_id_backmap, p, setup_logging

TARGET_FEATURES = {"FGFR2": ["FUS_FGFR2", "MUT_FGFR2"], "IDH1": ["MUT_IDH1"], "ERBB2": ["AMP_ERBB2"], "BRAF": ["MUT_BRAF"]}
DRUGS = ["pemigatinib", "futibatinib", "infigratinib", "ivosidenib", "zanidatamab", "trastuzumab", "dabrafenib", "trametinib",
         "durvalumab", "pembrolizumab", "atezolizumab", "nivolumab", "gemcitabine", "fluorouracil", "capecitabine", "lenvatinib",
         "sorafenib", "regorafenib", "doxorubicin"]


def zrows(x):
    return x.sub(x.mean(1), axis=0).div(x.std(1).replace(0, np.nan), axis=0)


def main():
    from miner import miner
    P = load_params(None)
    res = p(P["paths"]["results"])
    mx = P["miner"]["matrix"]
    outdir = os.path.join(res, "10_response", "dcna")
    os.makedirs(outdir, exist_ok=True)
    log = setup_logging(outdir, "10b_dcna")
    genes = pd.read_csv(os.path.join(res, "01_harmonized", "genes.tsv"), sep="\t", index_col=0)
    back = miner_id_backmap(p(P["miner"]["idmap"]), genes.index)
    mdir = os.path.join(res, "04_miner", mx)
    regs = {k: [back.get(g, g) for g in v] for k, v in json.load(open(os.path.join(mdir, "mechinf", "regulons_filtered.json"))).items()}
    rdf = pd.read_csv(os.path.join(mdir, "mechinf", "regulonDf.csv"))
    regulator = rdf.groupby(rdf["Regulon_ID"].astype(str))["Regulator"].first().map(lambda g: back.get(g, g))
    progs = {str(k): [str(r) for r in v] for k, v in json.load(open(os.path.join(mdir, "subtypes_filtered", "transcriptional_programs.json"))).items()}
    reg2prog = {r: k for k, v in progs.items() for r in v}
    cdir = os.path.join(res, "05_causal", mx)
    hc = pd.read_csv(os.path.join(cdir, "highConfidenceCausalResults.csv"), index_col=0)
    fl = pd.read_csv(os.path.join(cdir, "filteredCausalResults.csv"), index_col=0)
    for d_ in (hc, fl):
        d_["Regulon_ID"] = d_["Regulon_ID"].astype(str)

    T = pd.read_csv(p("data/reference/ot_drug_targets.tsv"), sep="\t")
    R, rows = {}, []
    for d, g in T[T["drug"].isin(DRUGS)].groupby("drug"):
        tg, sy = set(g["target_ensembl"]), set(g["target_symbol"])
        rt = sorted({r for r in regs if regulator.get(r) in tg} | {r for r, v in regs.items() if tg & set(v)})
        rc, src = {}, []
        for s_ in sy:
            for f in TARGET_FEATURES.get(s_, []):
                x = hc[hc["Mutation"] == f]
                tier = "high-confidence"
                if x.empty and "cohen_d" in fl:
                    x = fl[(fl["Mutation"] == f) & (fl["cohen_d"].abs() >= 0.5)]
                    tier = "filtered |d|>=0.5"
                if len(x):
                    x = x.assign(ad=x["cohen_d"].abs()).sort_values("ad", ascending=False).drop_duplicates("Regulon_ID")
                    rc.update({r: np.sign(dd) for r, dd in zip(x["Regulon_ID"], x["cohen_d"]) if r in regs})
                    src.append(f"{f} ({tier}, {len(x)})")
        act = str(g["action_type"].iloc[0]).upper()
        R[d] = (rt, rc, -1 if act in ("AGONIST", "ACTIVATOR") else 1)
        rows.append({"drug": d, "action": act, "targets": ",".join(sorted(sy)), "target_regulons": len(rt),
                     "causal_regulons": len(rc), "causal_source": "; ".join(src)})
    DR = pd.DataFrame(rows).set_index("drug")
    DR.to_csv(os.path.join(outdir, "drug_regulons.tsv"), sep="\t")
    log.info("Drug -> regulons:\n%s", DR.to_string())

    def dcna(A):
        A.index = A.index.astype(str)
        out = {"combined": {}, "target": {}, "causal": {}}
        for d, (rt, rc, sign) in R.items():
            t_ = [r for r in rt if r in A.index]
            c_ = {r: s for r, s in rc.items() if r in A.index}
            if t_:
                out["target"][d] = A.loc[t_].mean()
            if c_:
                out["causal"][d] = (A.loc[list(c_)].mul(pd.Series(c_), axis=0)).mean()
            parts = ([A.loc[t_]] if t_ else []) + ([A.loc[list(c_)].mul(pd.Series(c_), axis=0)] if c_ else [])
            if parts:
                out["combined"][d] = pd.concat(parts).groupby(level=0).first().mean()
        return {k: pd.DataFrame(v).T for k, v in out.items()}

    over = pd.read_csv(os.path.join(mdir, "subtypes_filtered", "overExpressedMembers.csv"), index_col=0)
    under = pd.read_csv(os.path.join(mdir, "subtypes_filtered", "underExpressedMembers.csv"), index_col=0)
    D = {"discovery": dcna(over - under)}
    # ---- GSE255058 (FOLFOX-HAIC + lenvatinib + anti-PD-1)
    C = P["validation"]["response"]["GSE255058"]
    x = pd.read_csv(p(C["expression"]).replace(".xlsx", ".tsv"), sep="\t").set_index(C["id_column"])  # TSV export (miner3 env lacks openpyxl)
    x = np.log2(x.groupby(level=0).sum() / x.groupby(level=0).sum().sum() * 1e6 + 1)
    x = x.loc[x.index.intersection(genes.index[genes["kept"]])]
    z = zrows(x).dropna(how="all")
    rm = {k: [g for g in v if g in z.index] for k, v in regs.items()}
    A = miner.generateRegulonActivity({k: v for k, v in rm.items() if len(v) > 1}, z, p=0.05)
    D["GSE255058"] = dcna(A)
    for c, dd in D.items():
        for k, M in dd.items():
            M.to_csv(os.path.join(outdir, f"dcna_{c}{'' if k == 'combined' else '_' + k}.tsv"), sep="\t", float_format="%.4g")
    y = pd.Series([int(s.startswith(C["responder_prefix"])) for s in z.columns], index=z.columns)
    tests = []
    M = D["GSE255058"]["combined"]
    # PDCD1 and TYMS are not in the network: the PD-1 axis is scored through CD274 (durvalumab / atezolizumab mapping);
    # FOLFOX has no mappable target (5-FU -> TYMS absent; oxaliplatin has no protein target)
    combos = {"lenvatinib": ["lenvatinib"], "PD-(L)1 axis (CD274 regulons)": ["durvalumab"],
              "regimen (independent action)": ["lenvatinib", "durvalumab"]}
    for lab, ds in combos.items():
        ds = [d for d in ds if d in M.index]
        s = M.loc[ds].max()
        au = stats.mannwhitneyu(s[y == 1], s[y == 0]).statistic / (y.sum() * (1 - y).sum())
        pred = (s > 0).astype(int)
        tests.append({"cohort": "GSE255058", "score": lab, "n": len(y), "responders": int(y.sum()), "auc": au,
                      "p_mwu": stats.mannwhitneyu(s[y == 1], s[y == 0]).pvalue, "pred_resp": int(pred.sum()),
                      "resp_rate_pred_resp": y[pred == 1].mean() if pred.sum() else np.nan,
                      "resp_rate_pred_nonresp": y[pred == 0].mean() if (1 - pred).sum() else np.nan})
    Tt = pd.DataFrame(tests)
    Tt.to_csv(os.path.join(outdir, "dcna_tests.tsv"), sep="\t", index=False, float_format="%.4g")
    log.info("GSE255058:\n%s", Tt.round(3).to_string(index=False))

    # ---- discovery subgroups
    G = pd.read_csv(os.path.join(res, "03_genomics_clinical", "genomic_features.csv"), index_col=0)
    stim = pd.read_csv(os.path.join(res, "07_post", "subtype_mapping", P["post"]["subtypes_dir"], "ntp_calls_stim.tsv"), sep="\t", index_col=0)["call"]
    infl = stim.isin(["IMMUNE_CLASSICAL", "INFLAMMATORY_STROMA"]).astype(float).where(stim != "unassigned")
    Md = D["discovery"]
    sub = []
    for drug, part, lab, g in (("pemigatinib", "combined", "FGFR2 fusion vs other", G.loc["FUS_FGFR2"]),
                               ("pemigatinib", "target", "FGFR2 fusion vs other (target part only)", G.loc["FUS_FGFR2"]),
                               ("futibatinib", "combined", "FGFR2 fusion vs other", G.loc["FUS_FGFR2"]),
                               ("ivosidenib", "combined", "IDH1 mutant vs other", G.loc["MUT_IDH1"]),
                               ("zanidatamab", "combined", "ERBB2 amplified vs other", G.loc["AMP_ERBB2"] if "AMP_ERBB2" in G.index else None),
                               ("durvalumab", "combined", "STIM inflamed vs other", infl),
                               ("pembrolizumab", "combined", "STIM inflamed vs other", infl)):
        Mx = D["discovery"][part]
        if g is None or drug not in Mx.index:
            continue
        s, gg = Mx.loc[drug], g.reindex(Mx.columns)
        ok = gg.notna()
        a, b = s[ok & (gg == 1)], s[ok & (gg == 0)]
        sub.append({"drug": drug, "part": part, "contrast": lab, "n_group": len(a), "n_other": len(b), "mean_group": a.mean(),
                    "mean_other": b.mean(), "auc_group_higher": stats.mannwhitneyu(a, b).statistic / (len(a) * len(b)),
                    "p_mwu": stats.mannwhitneyu(a, b).pvalue, "pred_resp_frac_group": (a > 0).mean(), "pred_resp_frac_other": (b > 0).mean()})
    S = pd.DataFrame(sub)
    S.to_csv(os.path.join(outdir, "subgroups.tsv"), sep="\t", index=False, float_format="%.4g")
    log.info("Discovery subgroups:\n%s", S.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
