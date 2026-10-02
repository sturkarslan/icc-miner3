#!/usr/bin/env python
"""Step 08 (ICC): external validation in cohorts never used for the network or the risk model.

For each cohort (config validation.cohorts):
  1. Expression -> Ensembl, log2(TPM + 1), gene z-score within the cohort.
  2. Portable scoring: regulon score = mean z of its genes (regulons with >= min_regulon_coverage of genes
     measured); program activity = mean of its regulons, standardized within the cohort.
  3. Fixed step-06 ridge program model (weights.tsv, never refit) -> risk score.
  4. Survival at the common horizon: C-index, Cox HR per SD, top-fraction vs rest. Reported overall, within
     each stratum (config strata_column, e.g. biopsy / surgical specimen), with a Cox model stratified by it,
     and adjusted for the technical covariate (genes detected) when tech_covariate is true.
The HCC version of this step (head-to-head with published signatures) is scripts/hcc_08_external_validation.py;
the ICC head-to-head is added once the ICC signature panel exists (step 07).

Outputs (results/08_validation/): <cohort>/{scores.tsv, evaluation.tsv, km_<endpoint>.png}, summary.tsv
"""

import argparse
import json
import os

import matplotlib
import numpy as np
import pandas as pd

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from hcc_common import load_params, miner_id_backmap, p, setup_logging  # noqa: E402

OUT = "08_validation"


def load_tpm_geo(cfg, log):
    """TPM table (Ensembl IDs) + samples_geo.tsv with survival in the sample characteristics."""
    x = pd.read_csv(p(cfg["expression"]), sep="\t", index_col=0)
    x.index = x.index.astype(str).str.replace(r"\.\d+$", "", regex=True)
    s = pd.read_csv(p(cfg["sample_table"]), sep="\t", dtype=str).set_index(cfg["sample_id_column"])
    s = s.loc[[c for c in x.columns if c in s.index]]
    x = x[s.index]
    clin = pd.DataFrame(index=s.index)
    for ep, e in cfg["survival"].items():
        clin[f"{ep}_time"] = pd.to_numeric(s[e["time_column"]], errors="coerce") * e.get("time_to_days", 1)
        clin[f"{ep}_event"] = pd.to_numeric(s[e["event_column"]], errors="coerce")
    if cfg.get("strata_column"):
        clin["stratum"] = s[cfg["strata_column"]].values
    for new, old in (cfg.get("covariates") or {}).items():
        clin[new] = s[old].values
    clin["n_genes_detected"] = (x >= 1).sum().values
    log.info("%s: %d genes x %d samples; genes detected %d-%d", cfg["_name"], *x.shape, clin["n_genes_detected"].min(),
             clin["n_genes_detected"].max())
    return np.log2(x.groupby(level=0).sum() + 1), clin


LOADERS = {"tpm_geo": load_tpm_geo}


def zrows(x):
    return x.sub(x.mean(1), axis=0).div(x.std(1).replace(0, np.nan), axis=0)


def score_programs(z, regulons, programs, min_cov):
    reg, cov = {}, {}
    for k, genes in regulons.items():
        g = [x for x in genes if x in z.index]
        cov[k] = len(g) / len(genes)
        if cov[k] >= min_cov and len(g) >= 3:
            reg[k] = z.loc[g].mean()
    reg = pd.DataFrame(reg).T
    prog = pd.DataFrame({k: reg.loc[[r for r in v if r in reg.index]].mean() for k, v in programs.items()
                         if any(r in reg.index for r in v)}).T
    return reg, prog, pd.Series(cov)


def horizon(clin, ep, days):
    s = clin[[f"{ep}_time", f"{ep}_event"]].dropna()
    s.columns = ["duration", "observed"]
    over = s["duration"] > days
    s.loc[over, "duration"] = days
    s.loc[over, "observed"] = 0
    return s[s["duration"] > 0]


def evaluate(score, srv, top, strata=None, covar=None):
    from lifelines import CoxPHFitter
    from lifelines.utils import concordance_index
    s = score[srv.index]
    zz = (s - s.mean()) / s.std()
    r = {"n": len(srv), "events": int(srv["observed"].sum()), "c_index": concordance_index(srv["duration"], -s, srv["observed"])}
    c = CoxPHFitter().fit(srv.assign(x=zz), "duration", "observed").summary.loc["x"]
    r.update(hr_per_sd=c["exp(coef)"], hr_per_sd_lo=c["exp(coef) lower 95%"], hr_per_sd_hi=c["exp(coef) upper 95%"], hr_per_sd_p=c["p"])
    high = (s >= s.quantile(1 - top)).astype(int)
    c = CoxPHFitter().fit(srv.assign(high=high), "duration", "observed").summary.loc["high"]
    r.update(hr_top=c["exp(coef)"], hr_top_lo=c["exp(coef) lower 95%"], hr_top_hi=c["exp(coef) upper 95%"], hr_top_p=c["p"])
    if strata is not None:
        d = srv.assign(x=zz, stratum=strata.reindex(srv.index)).dropna()
        c = CoxPHFitter().fit(d, "duration", "observed", strata=["stratum"]).summary.loc["x"]
        r.update(hr_per_sd_stratified=c["exp(coef)"], hr_per_sd_stratified_p=c["p"])
        if covar is not None:
            cv = covar.reindex(d.index)
            d2 = d.assign(tech=(cv - cv.mean()) / cv.std())
            c = CoxPHFitter().fit(d2, "duration", "observed", strata=["stratum"]).summary.loc["x"]
            r.update(hr_per_sd_stratified_tech_adj=c["exp(coef)"], hr_per_sd_stratified_tech_adj_p=c["p"])
    return r


def km_plot(score, srv, top, title, path, strata=None):
    from lifelines import KaplanMeierFitter
    groups = [("all", srv.index)] + ([(g, srv.index[strata.reindex(srv.index) == g]) for g in sorted(strata.dropna().unique())]
                                     if strata is not None else [])
    fig, axes = plt.subplots(1, len(groups), figsize=(3.4 * len(groups), 3.2), squeeze=False, layout="constrained")
    for ax, (g, idx) in zip(axes[0], groups):
        s = score[idx]
        hi = s >= s.quantile(1 - top)
        for lab, k, col in ((f"top {100 * top:.0f}%", hi, "#e34a4a"), ("rest", ~hi, "#2a78d6")):
            KaplanMeierFitter().fit(srv.loc[idx[k], "duration"] / 30.44, srv.loc[idx[k], "observed"],
                                    label=f"{lab} (n={k.sum()})").plot_survival_function(ax=ax, ci_show=False, color=col)
        ax.set_title(f"{title}: {g}", fontsize=8)
        ax.set_xlabel("months")
        ax.set_ylim(0, 1.02)
    fig.savefig(path, dpi=160)
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--params", default=None)
    ap.add_argument("--cohorts", default=None)
    args = ap.parse_args()
    P = load_params(args.params)
    V = P["validation"]
    matrix = P["miner"]["matrix"]
    res = p(P["paths"]["results"])
    outroot = os.path.join(res, OUT)
    log = setup_logging(outroot, "08_external_validation")
    genes = pd.read_csv(os.path.join(res, "01_harmonized", "genes.tsv"), sep="\t", index_col="ensembl")
    back = miner_id_backmap(p(P["miner"]["idmap"]), genes.index)
    mdir = os.path.join(res, "04_miner", matrix)
    regulons = {k: [back.get(g, g) for g in v] for k, v in json.load(open(os.path.join(mdir, "mechinf", "regulons_filtered.json"))).items()}
    programs = {k: [str(r) for r in v] for k, v in json.load(open(os.path.join(mdir, "subtypes_filtered", "transcriptional_programs.json"))).items()}
    rdir = os.path.join(res, "06_risk", matrix)
    models = {m: pd.read_csv(os.path.join(rdir, f"predictor_ridge_programs_{m}", "weights.tsv"), sep="\t", index_col=0)["weight"]
              .rename(lambda i: str(i)) for m in V["models"]}

    rows = []
    for name in (args.cohorts.split(",") if args.cohorts else list(V["cohorts"])):
        cfg = dict(V["cohorts"][name], _name=name)
        outdir = os.path.join(outroot, name)
        os.makedirs(outdir, exist_ok=True)
        x, clin = LOADERS[cfg["loader"]](cfg, log)
        x = x.loc[x.index.intersection(genes.index[genes["kept"]])]       # the network's gene universe
        z = zrows(x).dropna(how="all")
        reg, prog, cov = score_programs(z, regulons, programs, V["min_regulon_coverage"])
        net = set().union(*map(set, regulons.values()))
        log.info("%s: %.0f%% of network genes present; regulons scored %d / %d; programs %d / %d", name,
                 100 * len(net & set(z.index)) / len(net), reg.shape[0], len(regulons), prog.shape[0], len(programs))
        ps = zrows(prog)
        scores = pd.DataFrame(index=z.columns)
        for m, w in models.items():
            scores[f"risk_{m}"] = ps.fillna(0).T @ w.reindex(ps.index).fillna(0)
        scores = scores.join(clin)
        scores.to_csv(os.path.join(outdir, "scores.tsv"), sep="\t", float_format="%.5g")
        prog.to_csv(os.path.join(outdir, "program_activity.tsv"), sep="\t", float_format="%.4f")
        strata = clin["stratum"] if "stratum" in clin else None
        tech = clin["n_genes_detected"] if cfg.get("tech_covariate") else None
        if strata is not None:
            log.info("%s: risk score vs genes detected r %.2f; by stratum mean %s", name,
                     np.corrcoef(scores[f"risk_{V['models'][0]}"], clin["n_genes_detected"])[0, 1],
                     scores.groupby(strata)[f"risk_{V['models'][0]}"].mean().round(3).to_dict())
        for ep in cfg["endpoints"]:
            srv = horizon(clin, ep, V["horizon_days"])
            for m in models:
                subsets = [("all", srv.index)] + ([(g, srv.index[strata.reindex(srv.index) == g]) for g in sorted(strata.dropna().unique())]
                                                  if strata is not None else [])
                for sub, idx in subsets:
                    r = evaluate(scores[f"risk_{m}"], srv.loc[idx], V["top_fraction"], strata if sub == "all" else None, tech)
                    r.update(cohort=name, endpoint=ep, model=m, subset=sub)
                    rows.append(r)
                    log.info("%s %s %s [%s]: n=%d ev=%d C=%.3f HR/SD %.2f (%.2f-%.2f) p=%.1e | top HR %.2f p=%.1e | stratified "
                             "HR/SD %.2f p=%.1e | +tech %.2f p=%.1e", name, ep, m, sub, r["n"], r["events"], r["c_index"],
                             r["hr_per_sd"], r["hr_per_sd_lo"], r["hr_per_sd_hi"], r["hr_per_sd_p"], r["hr_top"], r["hr_top_p"],
                             r.get("hr_per_sd_stratified", np.nan), r.get("hr_per_sd_stratified_p", np.nan),
                             r.get("hr_per_sd_stratified_tech_adj", np.nan), r.get("hr_per_sd_stratified_tech_adj_p", np.nan))
                km_plot(scores[f"risk_{m}"], srv, V["top_fraction"], f"{name} {ep}", os.path.join(outdir, f"km_{ep}_{m}.png"), strata)
        pd.DataFrame([r for r in rows if r["cohort"] == name]).to_csv(os.path.join(outdir, "evaluation.tsv"), sep="\t", index=False,
                                                                     float_format="%.4g")
    pd.DataFrame(rows).to_csv(os.path.join(outroot, "summary.tsv"), sep="\t", index=False, float_format="%.4g")


if __name__ == "__main__":
    main()
