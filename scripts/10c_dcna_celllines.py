#!/usr/bin/env python
"""Step 10c (ICC): DCNA in biliary-tract cell lines vs measured drug sensitivity (PRISM Repurposing secondary screen).

Lines: PRISM 19Q4 secondary-screen lines with primary tissue bile_duct (7: 4 intrahepatic CCA, 2 extrahepatic, 1
gallbladder), expression from the Cell Model Passports RNA-seq (TPM; DepMap ModelID -> SangerModelID via DepMap
Model.csv). Gene z across all biliary-tract models with RNA-seq; MINER trinary regulon activity; DCNA per drug from
PRISM's own target annotation (gene symbols), with the causal-flow part of step 10b for FGFR2 / IDH1 / ERBB2 / BRAF.
Response: PRISM dose-response AUC (lower = more sensitive), z within drug across the lines. Drugs with >= 5 lines.
Tests: pooled predicted responders (DCNA > 0) vs non-responders; nulls: labels permuted within drug (1,000) and each
drug's regulons replaced by random regulons of the same size (200).
Outputs: results/10_response/dcna/{celllines_dcna.tsv, celllines_pairs.tsv, celllines_tests.tsv, celllines_by_drug.tsv}
"""

import json
import os
import zipfile

import numpy as np
import pandas as pd
from scipy import stats

from hcc_common import load_params, miner_id_backmap, p, setup_logging

TARGET_FEATURES = {"FGFR2": ["FUS_FGFR2", "MUT_FGFR2"], "IDH1": ["MUT_IDH1"], "ERBB2": ["AMP_ERBB2"], "BRAF": ["MUT_BRAF"]}


def main():
    from miner import miner
    P = load_params(None)
    res = p(P["paths"]["results"])
    mx = P["miner"]["matrix"]
    outdir = os.path.join(res, "10_response", "dcna")
    log = setup_logging(outdir, "10c_dcna_celllines")
    rng = np.random.default_rng(3)
    genes = pd.read_csv(os.path.join(res, "01_harmonized", "genes.tsv"), sep="\t", index_col=0)
    back = miner_id_backmap(p(P["miner"]["idmap"]), genes.index)
    mdir = os.path.join(res, "04_miner", mx)
    regs = {k: [back.get(g, g) for g in v] for k, v in json.load(open(os.path.join(mdir, "mechinf", "regulons_filtered.json"))).items()}
    rdf = pd.read_csv(os.path.join(mdir, "mechinf", "regulonDf.csv"))
    regulator = rdf.groupby(rdf["Regulon_ID"].astype(str))["Regulator"].first().map(lambda g: back.get(g, g))
    sym2ens = genes.reset_index().drop_duplicates("symbol").set_index("symbol")["ensembl"]
    cdir = os.path.join(res, "05_causal", mx)
    hc = pd.read_csv(os.path.join(cdir, "highConfidenceCausalResults.csv"), index_col=0)
    fl = pd.read_csv(os.path.join(cdir, "filteredCausalResults.csv"), index_col=0)
    for d_ in (hc, fl):
        d_["Regulon_ID"] = d_["Regulon_ID"].astype(str)

    # ---- lines and expression
    info = pd.read_csv(p("data/celllines/prism_secondary_cell_line_info.csv"))
    btc = info[info["primary_tissue"] == "bile_duct"]
    mdl = pd.read_csv(p("data/celllines/depmap_Model.csv"), low_memory=False).set_index("ModelID")
    btc = btc.assign(sanger=btc["depmap_id"].map(mdl["SangerModelID"]))
    ml = pd.read_csv(p("data/celllines/model_list_20240110.csv"), low_memory=False)
    pool = set(ml.loc[ml["cancer_type"].astype(str).str.contains("Biliary"), "model_id"]) | set(btc["sanger"].dropna())
    z_ = zipfile.ZipFile(p("data/celllines/rnaseq_all_20220624.zip"))
    with z_.open("rnaseq_tpm_20220624.csv") as fh:
        hdr = pd.read_csv(fh, nrows=4, header=None, low_memory=False)
    ids = hdr.iloc[0, 2:].tolist()
    keep = [i for i, m in enumerate(ids) if m in pool]
    with z_.open("rnaseq_tpm_20220624.csv") as fh:
        x = pd.read_csv(fh, skiprows=5, header=None, usecols=[1] + [k + 2 for k in keep], low_memory=False)
    x.columns = ["symbol"] + [ids[k] for k in keep]
    x = np.log2(x.dropna(subset=["symbol"]).set_index("symbol").apply(pd.to_numeric, errors="coerce").groupby(level=0).mean().fillna(0) + 1)
    x = x.loc[x.index.intersection(sym2ens.index)]
    x.index = sym2ens[x.index].values
    x = x.groupby(level=0).mean()
    x = x.loc[x.index.intersection(genes.index[genes["kept"]])]
    x = x.loc[x.var(1) > 0]
    z = x.sub(x.mean(1), axis=0).div(x.std(1), axis=0)
    log.info("Biliary-tract models with RNA-seq: %d (PRISM lines among them: %d of %d)", z.shape[1], len(set(btc["sanger"]) & set(z.columns)), len(btc))
    rm = {k: [g for g in v if g in z.index] for k, v in regs.items()}
    A = miner.generateRegulonActivity({k: v for k, v in rm.items() if len(v) > 1}, z, p=0.05)
    A.index = A.index.astype(str)

    # ---- drugs: PRISM targets -> regulons (+ causal part)
    pr = pd.read_csv(p("data/celllines/prism_secondary_dose_response.csv"), low_memory=False)
    pr = pr[pr["depmap_id"].isin(btc["depmap_id"])].dropna(subset=["auc", "target"])
    pr["line"] = pr["depmap_id"].map(btc.set_index("depmap_id")["sanger"])
    pr = pr[pr["line"].isin(A.columns)]
    pr = pr.sort_values("r2", ascending=False).drop_duplicates(["name", "line"])
    R, rows = {}, []
    for name, g in pr.groupby("name"):
        sy = {t.strip() for t in str(g["target"].iloc[0]).split(",")}
        tg = {sym2ens[s] for s in sy if s in sym2ens.index}
        rt = [r for r in regs if r in A.index and (regulator.get(r) in tg or tg & set(regs[r]))]
        rc = {}
        for s_ in sy:
            for f in TARGET_FEATURES.get(s_, []):
                xx = hc[hc["Mutation"] == f]
                if xx.empty:
                    xx = fl[(fl["Mutation"] == f) & (fl["cohen_d"].abs() >= 0.5)]
                rc.update({r: np.sign(d) for r, d in zip(xx["Regulon_ID"], xx["cohen_d"]) if r in A.index})
        if rt or rc:
            R[name] = (rt, rc)
    log.info("PRISM drugs tested on biliary lines: %d; with mapped regulons: %d (%d with a causal part)", pr["name"].nunique(), len(R),
             sum(1 for v in R.values() if v[1]))

    def score(rt, rc):
        parts = ([A.loc[rt]] if rt else []) + ([A.loc[list(rc)].mul(pd.Series(rc), axis=0)] if rc else [])
        return pd.concat(parts).groupby(level=0).first().mean()

    DC = pd.DataFrame({d: score(*v) for d, v in R.items()}).T
    DC.to_csv(os.path.join(outdir, "celllines_dcna.tsv"), sep="\t", float_format="%.4g")
    rows, bydrug = [], []
    for d in DC.index:
        g = pr[pr["name"] == d].set_index("line")["auc"]
        if len(g) < 5:
            continue
        s = DC.loc[d, g.index]
        za = (g - g.mean()) / g.std()
        pred = (s > 0).astype(int)
        rows += [{"drug": d, "line": l, "dcna": s[l], "pred": pred[l], "z_auc": za[l], "auc": g[l]} for l in g.index]
        bydrug.append({"drug": d, "n_lines": len(g), "n_pred_resp": int(pred.sum()),
                       "spearman_dcna_auc": stats.spearmanr(s, g)[0] if s.nunique() > 1 else np.nan})
    X, Bd = pd.DataFrame(rows), pd.DataFrame(bydrug)
    X.to_csv(os.path.join(outdir, "celllines_pairs.tsv"), sep="\t", index=False, float_format="%.4g")
    Bd.to_csv(os.path.join(outdir, "celllines_by_drug.tsv"), sep="\t", index=False, float_format="%.4g")
    obs = X.loc[X["pred"] == 1, "z_auc"].mean() - X.loc[X["pred"] == 0, "z_auc"].mean()
    null = []
    for _ in range(1000):
        pp = X.groupby("drug")["pred"].transform(lambda v: rng.permutation(v.values))
        null.append(X.loc[pp == 1, "z_auc"].mean() - X.loc[pp == 0, "z_auc"].mean())
    allr = list(A.index)
    zz = X.set_index(["drug", "line"])["z_auc"]
    nullr = []
    for _ in range(200):
        dl = []
        for d in X["drug"].unique():
            rt, rc = R[d]
            k = len(set(rt) | set(rc))
            sc = A.loc[rng.choice(allr, k, replace=False)].mean()
            lines = X.loc[X["drug"] == d, "line"]
            dl.append(pd.DataFrame({"pred": (sc[lines] > 0).astype(int).values, "z": zz.loc[d].loc[lines].values}))
        dl = pd.concat(dl)
        nullr.append(dl.loc[dl["pred"] == 1, "z"].mean() - dl.loc[dl["pred"] == 0, "z"].mean())
    neg = int((Bd["spearman_dcna_auc"] < 0).sum())
    nn = int(Bd["spearman_dcna_auc"].notna().sum())
    T = pd.DataFrame([{"level": "regulon (DCRA)", "drugs": X["drug"].nunique(), "lines": X["line"].nunique(), "pairs": len(X),
                       "pred_resp_pairs": int(X["pred"].sum()), "mean_z_pred_resp": X.loc[X["pred"] == 1, "z_auc"].mean(),
                       "mean_z_pred_nonresp": X.loc[X["pred"] == 0, "z_auc"].mean(), "delta": obs,
                       "perm_p_one_sided": (1 + np.sum(np.array(null) <= obs)) / 1001,
                       "random_regulon_null_mean": float(np.nanmean(nullr)), "random_regulon_p_one_sided": (1 + np.sum(np.array(nullr) <= obs)) / 201,
                       "drugs_with_negative_rho": neg, "drugs_with_rho": nn, "sign_test_p": stats.binomtest(neg, nn).pvalue}])
    T.to_csv(os.path.join(outdir, "celllines_tests.tsv"), sep="\t", index=False, float_format="%.4g")
    log.info("Biliary lines, pooled (lower z AUC = more sensitive):\n%s", T.round(3).T.to_string())
    for d in ["Gemcitabine", "gemcitabine", "cisplatin", "fluorouracil", "erdafitinib", "infigratinib", "AZD4547", "ivosidenib", "lapatinib",
              "trametinib", "dabrafenib", "lenvatinib", "sorafenib"]:
        b = Bd[Bd["drug"].str.lower() == d.lower()]
        if len(b):
            log.info("  %s: %s", d, b.round(3).to_dict("records")[0])


if __name__ == "__main__":
    main()
