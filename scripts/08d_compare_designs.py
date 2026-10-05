#!/usr/bin/env python
"""Compare discovery designs (config/params*.yaml): network size, overlap with the reference design, causal
flows, prognostic units and risk performance in every test cohort. Same tests for every design.

    python scripts/08d_compare_designs.py config/params.yaml:d315 config/params_d374.yaml:d374 config/params_d437.yaml:d433
Output: results/08_validation/design_comparison.tsv (first design is the reference for overlaps).
"""

import json
import os
import sys

import numpy as np
import pandas as pd

from hcc_common import load_params, miner_id_backmap, p


def net(P):
    res, mx = p(P["paths"]["results"]), P["miner"]["matrix"]
    mdir = os.path.join(res, "04_miner", mx)
    genes = pd.read_csv(os.path.join(res, "01_harmonized", "genes.tsv"), sep="\t", index_col=0)
    back = miner_id_backmap(p(P["miner"]["idmap"]), genes.index)
    sym = genes["symbol"]
    reg = {k: {sym.get(back.get(g, g), g) for g in v} for k, v in json.load(open(os.path.join(mdir, "mechinf", "regulons_filtered.json"))).items()}
    rdf = pd.read_csv(os.path.join(mdir, "mechinf", "regulonDf.csv"))
    regr = rdf.groupby(rdf["Regulon_ID"].astype(str))["Regulator"].first().map(lambda g: sym.get(back.get(g, g), g))
    progs = json.load(open(os.path.join(mdir, "subtypes_filtered", "transcriptional_programs.json")))
    pg = {k: set().union(*(reg[str(r)] for r in v if str(r) in reg)) for k, v in progs.items()}
    states = json.load(open(os.path.join(mdir, "subtypes_filtered", "transcriptional_states.json")))
    return res, mx, genes, reg, set(regr.reindex(list(reg)).dropna()), pg, states


def best_j(A, B):
    out = []
    for a in A.values():
        out.append(max((len(a & b) / len(a | b) for b in B.values() if a & b), default=0))
    return np.array(out)


def main():
    rows, ref = [], None
    for arg in sys.argv[1:]:
        f, tag = arg.split(":")
        P = load_params(f)
        res, mx, genes, reg, regs, pg, states = net(P)
        S = pd.read_csv(os.path.join(res, "01_harmonized", "samples.tsv"), sep="\t")
        r = {"design": tag, "tumours": len(S), "cohorts": ",".join(f"{c}:{n}" for c, n in S["cohort"].value_counts().items()),
             "genes": int(genes["kept"].sum()), "regulons": len(reg), "regulators": len(regs), "programs": len(pg), "states": len(states),
             "regulon_genes": len(set().union(*reg.values()))}
        if ref is None:
            ref = (reg, regs, pg)
        else:
            r["regulators_shared_with_ref"] = len(regs & ref[1]) / len(ref[1])
            r["ref_program_median_best_jaccard"] = float(np.median(best_j(ref[2], pg)))
            r["ref_program_frac_jaccard_ge_0_3"] = float((best_j(ref[2], pg) >= 0.3).mean())
        cf = pd.read_csv(os.path.join(res, "05_causal", mx, "causal_by_feature.tsv"), sep="\t", index_col=0)
        r["causal_high_conf_flows"] = int(cf["high_conf_flows"].sum())
        r["causal_features_with_hc"] = int((cf["high_conf_flows"] > 0).sum())
        for d in ("MUT_KRAS", "MUT_TP53", "MUT_BAP1", "MUT_IDH1", "FUS_FGFR2", "MUT_ARID1A"):
            r[f"hc_families_{d}"] = int(cf.loc[d, "high_conf_families"]) if d in cf.index else 0
        rs = pd.read_csv(os.path.join(res, "06_risk", mx, "risk_summary.tsv"), sep="\t")
        pr = rs[(rs["part"] == "prognostic") & (rs["unit"] == "programs")]
        r["prognostic_programs"] = f"{int(pr['n_prognostic'].iloc[0])}/{int(pr['n_tested'].iloc[0])}"
        rid = rs[rs["unit"].astype(str).str.startswith("ridge_programs")]     # primary model: ridge on program activity
        for _, x in rid.iterrows():
            if isinstance(x.get("cohort"), str) and pd.notna(x.get("c_index")):
                r[f"C_{x['cohort']}"] = x["c_index"]
                r[f"HRsd_{x['cohort']}"] = x.get("hr_per_sd", np.nan)
        v = pd.read_csv(os.path.join(res, "08_validation", "summary.tsv"), sep="\t")
        for _, x in v.iterrows():
            k = f"{x['cohort']}_{x['subset']}".replace("Surgical specimen", "surgical").replace("Biopsy", "biopsy")
            r[f"C_{k}"], r[f"HRsd_{k}"], r[f"p_{k}"] = x["c_index"], x["hr_per_sd"], x["hr_per_sd_p"]
            if x["subset"] == "all" and pd.notna(x.get("hr_per_sd_stratified")):
                r[f"HRsd_{x['cohort']}_stratified"], r[f"p_{x['cohort']}_stratified"] = x["hr_per_sd_stratified"], x["hr_per_sd_stratified_p"]
        rows.append(r)
    T = pd.DataFrame(rows).set_index("design").T
    out = os.path.join(p("results"), "08_validation", "design_comparison.tsv")
    T.to_csv(out, sep="\t")
    with pd.option_context("display.width", 200, "display.max_rows", 200):
        print(T.to_string())


if __name__ == "__main__":
    main()
