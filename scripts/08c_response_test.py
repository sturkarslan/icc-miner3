#!/usr/bin/env python
"""Step 08c (ICC): treatment-response test set (GSE255058; FOLFOX-HAIC + lenvatinib + PD-1, 9 responders / 9 not).

Pre-treatment biopsies, FPKM (Ensembl IDs). Too small to train on: the fixed network is scored (as step 08:
gene z within the cohort, regulon = mean z, program = mean of regulons) and compared between responders and
non-responders. Tests: the step-06 risk score (one test), then every program (Mann-Whitney, BH over programs),
which is exploratory with 18 samples.

Outputs (results/08_validation/GSE255058/): scores.tsv, program_response.tsv
"""

import importlib.util
import json
import os

import numpy as np
import pandas as pd
from scipy import stats

from hcc_common import load_params, miner_id_backmap, p, setup_logging


def main():
    P = load_params(None)
    C = P["validation"]["response"]["GSE255058"]
    res = p(P["paths"]["results"])
    outdir = os.path.join(res, "08_validation", "GSE255058")
    log = setup_logging(outdir, "08c_response_test")
    spec = importlib.util.spec_from_file_location("s08", os.path.join(os.path.dirname(__file__), "08_external_validation.py"))
    s08 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(s08)
    matrix = P["miner"]["matrix"]
    genes = pd.read_csv(os.path.join(res, "01_harmonized", "genes.tsv"), sep="\t", index_col="ensembl")
    back = miner_id_backmap(p(P["miner"]["idmap"]), genes.index)
    mdir = os.path.join(res, "04_miner", matrix)
    regulons = {k: [back.get(g, g) for g in v] for k, v in json.load(open(os.path.join(mdir, "mechinf", "regulons_filtered.json"))).items()}
    programs = {k: [str(r) for r in v] for k, v in json.load(open(os.path.join(mdir, "subtypes_filtered", "transcriptional_programs.json"))).items()}
    x = pd.read_excel(p(C["expression"])).set_index(C["id_column"])
    x = x.groupby(level=0).sum()
    x = np.log2(x / x.sum() * 1e6 + 1)                       # FPKM -> TPM -> log2
    x = x.loc[x.index.intersection(genes.index[genes["kept"]])]
    resp = pd.Series([c.startswith(C["responder_prefix"]) for c in x.columns], index=x.columns)
    z = s08.zrows(x).dropna(how="all")
    reg, prog, cov = s08.score_programs(z, regulons, programs, P["validation"]["min_regulon_coverage"])
    ps = s08.zrows(prog)
    m = P["validation"]["models"][0]
    w = pd.read_csv(os.path.join(res, "06_risk", matrix, f"predictor_ridge_programs_{m}", "weights.tsv"), sep="\t",
                    index_col=0)["weight"].rename(lambda i: str(i))
    risk = ps.fillna(0).T @ w.reindex(ps.index).fillna(0)
    u = stats.mannwhitneyu(risk[resp], risk[~resp])
    auc = u.statistic / (resp.sum() * (~resp).sum())
    log.info("%d samples (%d responders); %d regulons, %d programs scored", len(resp), resp.sum(), len(reg), len(prog))
    log.info("Risk score (%s): responders median %.3f, non-responders %.3f; AUC (responder higher) %.2f, Mann-Whitney p %.3f",
             m, risk[resp].median(), risk[~resp].median(), auc, u.pvalue)
    pd.DataFrame({"risk": risk, "responder": resp}).to_csv(os.path.join(outdir, "scores.tsv"), sep="\t")
    rows = []
    for k in ps.index:
        uu = stats.mannwhitneyu(ps.loc[k, resp], ps.loc[k, ~resp])
        rows.append({"program": k, "auc_responder_higher": uu.statistic / (resp.sum() * (~resp).sum()), "p": uu.pvalue,
                     "risk_weight": w.get(k, np.nan)})
    T = pd.DataFrame(rows).set_index("program").sort_values("p")
    o = np.argsort(T["p"].values)
    q = np.minimum.accumulate((T["p"].values[o] * len(T) / np.arange(1, len(T) + 1))[::-1])[::-1]
    T["q"] = np.minimum(q, 1)
    T.to_csv(os.path.join(outdir, "program_response.tsv"), sep="\t", float_format="%.4g")
    log.info("Programs: min q %.2f; nominal p < 0.05: %d of %d (expected by chance %.0f)\n%s", T["q"].min(), (T["p"] < 0.05).sum(),
             len(T), 0.05 * len(T), T.head(8).round(3).to_string())


if __name__ == "__main__":
    main()
