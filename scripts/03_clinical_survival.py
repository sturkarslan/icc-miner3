#!/usr/bin/env python
"""Step 03 (clinical part, ICC): survival files for MINER3 and a clinical table for the discovery cohort.

Endpoints per cohort are in config clinical.<cohort>.endpoints (FU-iCCA and TCGA: OS; GSE107943: OS and
RFS). Survival is never pooled across cohorts. One MINER file per cohort and endpoint, with and
without the common horizon (survival.horizon_months): events after the horizon are censored at it.

Outputs (results/03_genomics_clinical/):
  survival_<cohort>.tsv                     sample, os_days, os_event + covariates (config clinical.<cohort>.covariates)
  survival_<cohort>_OS_miner.csv            sample, duration (days), observed
  survival_<cohort>_OS_h<N>m_miner.csv      same, censored at the horizon
  qc/s1_km_<cohort>.png                     Kaplan-Meier, overall and by stage
"""

import argparse
import os

import numpy as np
import pandas as pd

from hcc_common import load_params, p, require_columns, setup_logging

OUT = "03_genomics_clinical"
DAYS_PER_MONTH = 30.44


def horizon_censor(d, horizon_days):
    out = d.copy()
    late = out["duration"] > horizon_days
    out.loc[late, "observed"] = 0
    out.loc[late, "duration"] = horizon_days
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--params", default=None)
    args = ap.parse_args()
    P = load_params(args.params)
    res = p(P["paths"]["results"])
    outdir = os.path.join(res, OUT)
    os.makedirs(os.path.join(outdir, "qc"), exist_ok=True)
    log = setup_logging(outdir, "03_clinical_survival")
    samples = pd.read_csv(os.path.join(res, "01_harmonized", "samples.tsv"), sep="\t")
    hm = P["survival"]["horizon_months"]

    for cohort, C in P["clinical"].items():
        pre = P["cohorts"][cohort].get("sample_prefix", "")
        t = pd.read_csv(p(C["table"]), sep="\t", skiprows=C.get("skiprows", 0), dtype=str).dropna(axis=1, how="all")
        cov, eps = C.get("covariates") or {}, C["endpoints"]
        require_columns(t, [C["id_column"]] + [e[k] for e in eps.values() for k in ("time_column", "event_column")]
                        + list(cov.values()), f"{cohort} clinical")
        t = t.dropna(subset=[C["id_column"]])
        t.index = pre + t[C["id_column"]].str.strip()
        in_net = samples.loc[samples["cohort"] == cohort, "sample"]
        n = C.get("id_match_chars")
        key = in_net.str[:n] if n else in_net          # e.g. TCGA: patient = first 12 characters of the sample ID
        t = t[~t.index.duplicated()].reindex(key.values)
        d = pd.DataFrame(index=pd.Index(in_net.values, name="sample"))
        for ep, e in eps.items():
            d[f"{ep.lower()}_days"] = pd.to_numeric(t[e["time_column"]], errors="coerce").values * e.get("time_to_days", 1)
            d[f"{ep.lower()}_event"] = pd.to_numeric(t[e["event_column"]], errors="coerce").values
        for new, old in cov.items():
            d[new] = t[old].str.strip().values
        d.to_csv(os.path.join(outdir, f"survival_{cohort}.tsv"), sep="\t")
        for ep in eps:
            ok = d.dropna(subset=[f"{ep.lower()}_days", f"{ep.lower()}_event"])
            ok = ok[ok[f"{ep.lower()}_days"] > 0]
            m = pd.DataFrame({"duration": ok[f"{ep.lower()}_days"], "observed": ok[f"{ep.lower()}_event"].astype(int)})
            m.to_csv(os.path.join(outdir, f"survival_{cohort}_{ep}_miner.csv"))
            mh = horizon_censor(m, hm * DAYS_PER_MONTH)
            mh.to_csv(os.path.join(outdir, f"survival_{cohort}_{ep}_h{hm}m_miner.csv"))
            fu = m.loc[m["observed"] == 0, "duration"]
            log.info("%s %s: %d network samples, %d with data; events %d (%.0f%%); within %d months %d; median follow-up "
                     "of censored %.0f days (max %.0f)", cohort, ep, len(in_net), len(m), m["observed"].sum(),
                     100 * m["observed"].mean(), hm, mh["observed"].sum(), fu.median(), m["duration"].max())
        for c in cov:
            if d[c].nunique() <= 8:
                log.info("  %s: %s", c, d[c].value_counts(dropna=False).to_dict())
        m = pd.read_csv(os.path.join(outdir, f"survival_{cohort}_OS_miner.csv"), index_col=0)

        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from lifelines import KaplanMeierFitter
        fig, axes = plt.subplots(1, 2, figsize=(8.5, 3.6), layout="constrained")
        KaplanMeierFitter().fit(m["duration"] / DAYS_PER_MONTH, m["observed"], label=f"{cohort} (n={len(m)})").plot_survival_function(ax=axes[0])
        axes[0].axvline(hm, color="grey", ls="--", lw=0.8)
        if "stage" in d:
            st = d.loc[m.index, "stage"].str.replace(r"[AB]$", "", regex=True)
            for s in sorted(st.dropna().unique()):
                k = st == s
                if k.sum() >= 5:
                    KaplanMeierFitter().fit(m.loc[k, "duration"] / DAYS_PER_MONTH, m.loc[k, "observed"],
                                            label=f"stage {s} (n={k.sum()})").plot_survival_function(ax=axes[1], ci_show=False)
        for ax in axes:
            ax.set_xlabel("months")
            ax.set_ylabel("overall survival")
            ax.set_ylim(0, 1.02)
        fig.savefig(os.path.join(outdir, "qc", f"s1_km_{cohort}.png"), dpi=160)


if __name__ == "__main__":
    main()
