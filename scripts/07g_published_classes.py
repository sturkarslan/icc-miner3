#!/usr/bin/env python
"""Step 07g (ICC): the network and risk model against published iCCA classes and prognostic signatures.

A. Discovery cohort (FU-iCCA, published per-patient calls from config/icc_published_labels.tsv; our NTP calls for
   the other cohorts): risk score (step 06, within-cohort z) by class, Kruskal-Wallis; MINER states enriched for
   each published class (state_enrichment.tsv, FDR < 0.05, OR > 1).
B. Head-to-head in the held-out cohorts (never in the network or the model): GSE244807 (Cox stratified by specimen)
   and OEP002768 (unique patients). Competitors:
     - published classes available there (GSE244807: STIM, Beaufrere / Martin-Serrano labels; OEP002768: Lin 2026)
       as categorical Cox models FITTED IN THE TEST COHORT (optimistic for the competitor);
     - published prognostic signatures (mean z of up genes minus mean z of down genes). Unsigned signatures are
       oriented by the sign of their Cox coefficient in FU-iCCA (discovery), never in the test cohort.
   For each: C-index, and the likelihood-ratio test of adding the MINER risk score to it (and the reverse).

Outputs (results/07_post/published/): risk_by_class.tsv, states_vs_published.tsv, head_to_head.tsv
"""

import importlib.util
import os

import numpy as np
import pandas as pd
from scipy import stats

from hcc_common import load_params, p, setup_logging

def load_mod(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(os.path.dirname(os.path.abspath(__file__)), fname))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def sig_score(z, sig, name):
    up = sig[(sig["set"] == name) & sig["ensembl"].isin(z.index)]["ensembl"].unique()
    dn = sig[(sig["set"] == name + "_DN") & sig["ensembl"].isin(z.index)]["ensembl"].unique()
    s = z.loc[up].mean() if len(up) else 0
    if len(dn):
        s = s - z.loc[dn].mean()
    return s if len(up) + len(dn) >= 2 else None


def cox(d, cols, strata=None):
    from lifelines import CoxPHFitter
    m = CoxPHFitter(penalizer=1e-4).fit(d[cols + ["duration", "observed"] + ([strata] if strata else [])], "duration", "observed",
                                        strata=[strata] if strata else None)
    return m


def c_index(d, m):
    from lifelines.utils import concordance_index
    return concordance_index(d["duration"], -m.predict_partial_hazard(d).values.ravel(), d["observed"])


def main():
    P = load_params(None)
    res = p(P["paths"]["results"])
    outdir = os.path.join(res, "07_post", "published")
    log = setup_logging(outdir, "07g_published_classes")
    s08 = load_mod("s08", "08_external_validation.py")
    mx = P["miner"]["matrix"]
    m = P["validation"]["models"][0]
    hd = P["validation"]["horizon_days"]
    S = pd.read_csv(os.path.join(res, "01_harmonized", "samples.tsv"), sep="\t", index_col="sample")
    pred = pd.read_csv(os.path.join(res, "06_risk", mx, f"predictor_ridge_programs_{m}", "predictions.tsv"), sep="\t", index_col=0)
    risk = pred.groupby("cohort")["risk_score"].transform(lambda v: (v - v.mean()) / v.std())
    L = pd.read_csv(p(P["post"]["published_labels"]), sep="\t", dtype=str)

    # ---- A. risk by published class in FU-iCCA, and states
    fu = L[L["cohort"] == "FU_iCCA"].assign(sample=lambda d: "FU" + d["sample"])
    rows = []
    for cl, d in fu.groupby("classifier"):
        x = d.set_index("sample")["class"].reindex(risk.index).dropna()
        g = risk[x.index].groupby(x)
        kw = stats.kruskal(*[v.values for _, v in g if len(v) >= 3]).pvalue
        for k, v in g:
            rows.append({"classifier": cl, "class": k, "n": len(v), "median_risk_z": v.median(), "kw_p": kw})
    R = pd.DataFrame(rows)
    R.to_csv(os.path.join(outdir, "risk_by_class.tsv"), sep="\t", index=False, float_format="%.4g")
    log.info("FU-iCCA risk z by published class (median; Kruskal-Wallis p):\n%s",
             "\n".join(f"  {c}: " + ", ".join(f"{r['class']} {r['median_risk_z']:+.2f} (n {r['n']})" for _, r in d.sort_values("median_risk_z").iterrows())
                       + f"  p {d['kw_p'].iloc[0]:.1e}" for c, d in R.groupby("classifier")))
    E = pd.read_csv(os.path.join(res, "07_post", "subtype_mapping", P["post"]["subtypes_dir"], "state_enrichment.tsv"), sep="\t")
    E = E[E["annotation"].str.startswith(("pub_", "ntp_")) & (E["fdr"] < 0.05) & (E["odds_ratio"] > 1)]
    st = E.sort_values("fdr").groupby(["annotation", "level"])["state"].agg(lambda v: ",".join(f"S{x}" for x in v)).rename("states")
    st.to_csv(os.path.join(outdir, "states_vs_published.tsv"), sep="\t")
    log.info("Published classes with >= 1 enriched MINER state: %d of %d class levels", len(st),
             E["annotation"].str.cat(E["level"].astype(str)).nunique() if len(E) else 0)

    # ---- B. head-to-head in held-out cohorts
    sig = pd.read_csv(os.path.join(res, "07_post", "signatures", "signatures.tsv"), sep="\t").dropna(subset=["ensembl"])
    names = sorted({s.replace("custom:", "") for s in sig["set"] if s.startswith("custom:ICC_PROGNOSTIC")}) + \
        ["SIA2013_SURVIVAL_POOR", "SIA2013_RECURRENCE_POOR", "DONG2022_PROGNOSTIC_BIOMARKERS", "FAN2024_CORE37"]
    names = ["custom:" + n for n in names]
    # orientation of signatures in discovery (FU-iCCA OS)
    zd = pd.read_csv(os.path.join(res, "02_batch_corrected", f"expression_{mx}_z.csv"), index_col=0)
    sfu = pd.read_csv(os.path.join(res, "03_genomics_clinical", "survival_FU_iCCA_OS_h36m_miner.csv"), index_col=0)
    sfu.columns = ["duration", "observed"]
    orient = {}
    for n in names:
        sc = sig_score(zd[sfu.index], sig, n)
        if sc is None:
            continue
        d = sfu.assign(x=(sc - sc.mean()) / sc.std())
        orient[n] = np.sign(cox(d, ["x"]).params_["x"])
    log.info("Signature orientation in FU-iCCA (+1 = high score adverse): %s", {k.replace("custom:", ""): int(v) for k, v in orient.items()})
    pubcls = {"GSE244807": ("stim", "GSE244807", lambda i: i), "OEP002768": ("lin2026", "OEP002768", None)}
    rows = []
    for name in ("GSE244807", "OEP002768"):
        cfg = dict(P["validation"]["cohorts"][name], _name=name, _res=res)
        x, clin = s08.LOADERS[cfg["loader"]](cfg, log)
        x = x.loc[x.index.intersection(zd.index)]
        z = s08.zrows(x).dropna(how="all")
        sc = pd.read_csv(os.path.join(res, "08_validation", name, "scores.tsv"), sep="\t", index_col=0)
        srv = s08.horizon(clin, "OS", hd)
        d = srv.copy()
        d["miner"] = sc.loc[d.index, f"risk_{m}"]
        d["miner"] = (d["miner"] - d["miner"].mean()) / d["miner"].std()
        strata = None
        if "stratum" in clin:
            d["stratum"] = clin.loc[d.index, "stratum"]
            strata = "stratum"
        comps = {}
        for n, o in orient.items():
            s_ = sig_score(z[d.index], sig, n)
            if s_ is not None:
                comps[n.replace("custom:", "")] = ("signature", (o * (s_ - s_.mean()) / s_.std()).rename(None))
        cl, lc, _ = pubcls[name]
        lab = L[(L["cohort"] == lc) & (L["classifier"] == cl)]
        if name == "OEP002768":
            o = pd.read_csv(p(cfg["sample_table"]), sep="\t").set_index("patient")["sample"]
            lab = lab.assign(sample=lab["sample"].map(o))
        if name == "GSE244807":                     # labels use patient IDs (CK001); expression columns CK001_S1_L001
            lab = lab.assign(sample=lab["sample"].map({c.split("_")[0]: c for c in d.index}))
        lab = lab.dropna(subset=["sample"]).set_index("sample")["class"]
        if len(lab.index.intersection(d.index)) >= 20:
            comps[f"{cl} classes (fitted here)"] = ("class", lab)
        base = cox(d, ["miner"], strata)
        rows.append({"cohort": name, "model": "MINER risk", "n": len(d), "events": int(d["observed"].sum()), "c_index": c_index(d, base),
                     "hr_per_sd": float(np.exp(base.params_["miner"])), "p": float(base.summary.loc["miner", "p"])})
        for k, (kind, v) in comps.items():
            dd = d.join(v.rename("comp"), how="inner").dropna(subset=["comp"])
            if kind == "class":
                dum = pd.get_dummies(dd["comp"], prefix="c", drop_first=True, dtype=float)
                dum = dum.loc[:, dum.sum() >= 3]
                cc = list(dum.columns)
                dd = pd.concat([dd, dum], axis=1)
            else:
                cc = ["comp"]
            mc = cox(dd, cc, strata)
            mm = cox(dd, ["miner"], strata)
            mb = cox(dd, cc + ["miner"], strata)
            lr_add_miner = 2 * (mb.log_likelihood_ - mc.log_likelihood_)
            lr_add_comp = 2 * (mb.log_likelihood_ - mm.log_likelihood_)
            rows.append({"cohort": name, "model": k, "kind": kind, "n": len(dd), "events": int(dd["observed"].sum()),
                         "c_index": c_index(dd, mc), "c_index_miner_same_samples": c_index(dd, mm),
                         "hr_per_sd": float(np.exp(mc.params_["comp"])) if kind == "signature" else np.nan,
                         "p": float(mc.summary.loc["comp", "p"]) if kind == "signature" else float(mc.log_likelihood_ratio_test().p_value),
                         "p_add_miner": stats.chi2.sf(lr_add_miner, 1), "p_add_competitor": stats.chi2.sf(lr_add_comp, len(cc)),
                         "hr_miner_given_competitor": float(np.exp(mb.params_["miner"]))})
    H = pd.DataFrame(rows)
    H.to_csv(os.path.join(outdir, "head_to_head.tsv"), sep="\t", index=False, float_format="%.4g")
    with pd.option_context("display.width", 220, "display.max_rows", 100):
        log.info("Head-to-head (held-out cohorts; GSE244807 Cox stratified by specimen):\n%s",
                 H[["cohort", "model", "n", "events", "c_index", "c_index_miner_same_samples", "hr_per_sd", "p", "p_add_miner",
                    "p_add_competitor", "hr_miner_given_competitor"]].round(3).to_string(index=False))


if __name__ == "__main__":
    main()
