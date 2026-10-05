#!/usr/bin/env python
"""Step 10d (ICC): emulate published biliary-tract / ICC trial arms with synthetic cohorts from the 374 discovery tumours,
predict each arm's ORR from DCNA (step 10b, combined target + causal part) and compare with the published ORR.
Design: docs/trial_emulation_design.md (Claude Cloud); arms, published ORR and eligibility filters: config/trials.yaml;
baseline sex / age / Asian ancestry per arm: ClinicalTrials.gov posted results (scripts/tools/fetch_trials.py).

Pool per arm: discovery tumours passing the arm's genomic filters (FUS_FGFR2, MUT_IDH1, AMP_ERBB2, MUT_BRAF; profiled tumours
only: FU-iCCA and TCGA-CHOL). Unmatched eligibility (ECOG, prior lines, site mix of BTC trials) is listed, not applied.
Weights: entropy balancing to the arm's posted % female and mean age (Asian share where posted); 1,000 cohorts of the arm's
size drawn with replacement. Responder: DCNA > tau; combinations: independent drug action (max over drugs).
Proxies (stated): pembrolizumab -> CD274 regulons (durvalumab mapping; PDCD1 is not in the network); cisplatin has no
protein target and is dropped from GemCis (scored as gemcitabine).
Threshold modes: A per-arm (calibration, circular); B leave-one-trial-out global tau; C same-class transfer
(FGFR inhibitor arms, ICI + GemCis arms, GemCis arms); D control-arm anchor (tau from the trial's GemCis arm, applied to
its experimental arm). Pool size is reported with every arm.
Outputs: results/10_response/trials/{emulation_arms.tsv, emulation_predictions.tsv, emulation_summary.tsv}; figure
results/10_response/figures/trial_emulation.{png,pdf}
"""

import os

import numpy as np
import pandas as pd
import yaml
from scipy import optimize, stats

from hcc_common import load_params, p, setup_logging

CTGOV_GROUP = {"TOPAZ1_durva_gemcis": ("TOPAZ-1", "Durvalumab"), "TOPAZ1_placebo_gemcis": ("TOPAZ-1", "Placebo"),
               "KN966_pembro_gemcis": ("KEYNOTE-966", "Arm A"), "KN966_placebo_gemcis": ("KEYNOTE-966", "Arm B"),
               "FIGHT202_pemigatinib": ("FIGHT-202", "Cohort A"), "FIGHT202_cohortC_negative": ("FIGHT-202", "Cohort C"),
               "FOENIX_futibatinib": ("FOENIX-CCA2", "Phase 2"), "CLARIDHY_ivosidenib": ("ClarIDHy", "AG-120"),
               "HERIZON_zanidatamab": ("HERIZON-BTC-01", "Cohort I"), "ROAR_dabrafenib_trametinib": ("ROAR", "Biliary")}
PROXY = {"pembrolizumab": "durvalumab", "cisplatin": None, "oxaliplatin": None}
CLASS = {"TOPAZ1_durva_gemcis": "ICI + GemCis", "KN966_pembro_gemcis": "ICI + GemCis", "TOPAZ1_placebo_gemcis": "GemCis",
         "KN966_placebo_gemcis": "GemCis", "FIGHT202_pemigatinib": "FGFR inhibitor, fusion+", "FOENIX_futibatinib": "FGFR inhibitor, fusion+",
         "FIGHT202_cohortC_negative": "FGFR inhibitor, FGFR-negative", "CLARIDHY_ivosidenib": "IDH1 inhibitor",
         "HERIZON_zanidatamab": "HER2", "ROAR_dabrafenib_trametinib": "BRAF + MEK"}
CONTROL = {"TOPAZ1_durva_gemcis": "TOPAZ1_placebo_gemcis", "KN966_pembro_gemcis": "KN966_placebo_gemcis"}


def entropy_weights(X, target):
    Z = (X - target).values
    lam = optimize.minimize(lambda l: np.log(np.mean(np.exp(np.clip(Z @ l, -50, 50)))), np.zeros(Z.shape[1]),
                            jac=lambda l: (Z * np.exp(np.clip(Z @ l, -50, 50))[:, None]).sum(0) / np.exp(np.clip(Z @ l, -50, 50)).sum(), method="BFGS").x
    w = np.exp(Z @ lam)
    return w / w.sum()


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--part", default="combined", choices=["combined", "target"],
                    help="DCNA part: combined (target + causal regulons) or target regulons only (sensitivity)")
    args = ap.parse_args()
    sfx = "" if args.part == "combined" else "_target"
    P = load_params(None)
    res = p(P["paths"]["results"])
    outdir = os.path.join(res, "10_response", "trials")
    log = setup_logging(outdir, "10d_trial_emulation")
    cfg = yaml.safe_load(open(p("config/trials.yaml")))
    ncoh, rng = int(cfg["defaults"]["n_cohorts"]), np.random.default_rng(int(cfg["defaults"]["seed"]))
    arms = dict(cfg["arms"])
    # FIGHT-202 cohort C (ClinicalTrials.gov NCT02924376 posted results): pemigatinib in FGF/FGFR-negative tumours, ORR 0/17
    arms["FIGHT202_cohortC_negative"] = {"trial": "FIGHT-202 cohort C", "drugs": ["pemigatinib"], "n": 17, "orr": 0.0,
                                         "eligibility": {"filters": {"FUS_FGFR2": 0}}, "source": "ClinicalTrials.gov NCT02924376 results"}
    base = pd.read_csv(os.path.join(outdir, "trial_arms.tsv"), sep="\t")
    dc = pd.read_csv(os.path.join(res, "10_response", "dcna", f"dcna_discovery{sfx}.tsv"), sep="\t", index_col=0)
    G = pd.read_csv(os.path.join(res, "03_genomics_clinical", "genomic_features.csv"), index_col=0)
    sm = pd.read_csv(os.path.join(res, "01_harmonized", "samples.tsv"), sep="\t", index_col="sample")
    cov = []
    for c in ("FU_iCCA", "GSE107943", "TCGA"):
        t = pd.read_csv(os.path.join(res, "03_genomics_clinical", f"survival_{c}.tsv"), sep="\t", index_col=0)
        for s_ in t.index:
            sx = str(t["sex"].get(s_, "")) if "sex" in t else ""
            cov.append({"sample": s_, "age": pd.to_numeric(t["age"].get(s_), errors="coerce"),
                        "female": 1.0 if sx.lower().startswith("f") else (0.0 if sx.lower().startswith("m") else np.nan),
                        "asian": 1.0 if c in ("FU_iCCA", "GSE107943") else np.nan})
    C = pd.DataFrame(cov).set_index("sample").reindex(dc.columns)
    C.loc[sm.reindex(C.index)["cohort"] == "GSE179443", "asian"] = 1.0
    log.info("Pool: %d tumours; female known %d, age known %d", len(C), C["female"].notna().sum(), C["age"].notna().sum())

    rows, sims, draws = [], {}, {}
    taus = np.round(np.linspace(-1, 1, 401), 3)
    for key, a in arms.items():
        drugs = [PROXY.get(d, d) for d in a["drugs"]]
        drugs = [d for d in drugs if d and d in dc.index]
        pool = C.copy()
        for f, v in (a.get("eligibility", {}).get("filters") or {}).items():
            if f == "site":
                continue
            if f not in G.index:
                pool = pool.iloc[0:0]
                break
            g = G.loc[f].reindex(pool.index)
            pool = pool[g == v]
        tr, grp = CTGOV_GROUP.get(key, (None, None))
        b = base[(base["trial"] == tr) & base["group"].str.contains(grp, case=False, regex=False)] if tr else base.iloc[0:0]
        b = b.iloc[0] if len(b) else None
        cols, target = [], []
        if b is not None:
            for col, k in (("female", "female_frac"), ("age", "age"), ("asian", "asian_frac")):
                known = pool[col].dropna()
                binary_ok = col == "age" or ((known == 1).sum() >= 10 and (known == 0).sum() >= 10)
                if pd.notna(b[k]) and len(known) >= 10 and binary_ok:
                    cols.append(col)
                    target.append(b[k])
        row = {"arm": key, "trial": a["trial"], "class": CLASS.get(key, ""), "drugs": "+".join(drugs), "n": int(a["n"]), "orr": a["orr"],
               "pool": len(pool), "balance_vars": ",".join(cols)}
        if not drugs or len(pool) < 5:
            row["status"] = "not emulable (pool < 5 or no mapped drug)"
            rows.append(row)
            continue
        X = pool[cols].astype(float) if cols else pd.DataFrame(index=pool.index)
        ok = X.notna().all(1) if cols else pd.Series(True, index=pool.index)
        w = np.zeros(len(pool))
        try:
            w[ok.values] = entropy_weights(X[ok], np.array(target)) if cols else 1 / ok.sum()
        except Exception:  # noqa: BLE001
            w[ok.values] = 1 / ok.sum()
        w = w / w.sum()
        idx = rng.choice(len(pool), size=(ncoh, int(a["n"])), p=w)
        V = dc.loc[drugs, pool.index].values.max(0)
        sims[key] = (V[idx][:, :, None] > taus[None, None, :]).mean(1)
        draws[key] = (pool.index, idx[:200], len(drugs))
        row.update(status="emulated", effective_n=1 / np.sum(w ** 2), distinct_tumours_mean=float(np.mean([len(set(r)) for r in idx[:50]])))
        rows.append(row)
    AR = pd.DataFrame(rows).set_index("arm")
    AR.to_csv(os.path.join(outdir, f"emulation_arms{sfx}.tsv"), sep="\t", float_format="%.4g")
    em = AR[AR["status"] == "emulated"]
    mc = {k: v.mean(0) for k, v in sims.items()}

    def pred(key, k, mode, extra=None):
        s = sims[key][:, k]
        r = AR.loc[key]
        d = {"mode": mode, "arm": key, "trial": r["trial"], "class": r["class"], "drugs": r["drugs"], "pool": r["pool"], "n": r["n"],
             "orr": r["orr"], "tau": taus[k], "pred": s.mean(), "lo": np.percentile(s, 2.5), "hi": np.percentile(s, 97.5)}
        d.update(extra or {})
        return d

    P_ = []
    for key in em.index:                                                     # A
        k = int(np.argmin(np.abs(mc[key] - AR.loc[key, "orr"])))
        P_.append(pred(key, k, "A per-arm tau (calibration)"))
    for trial in em["trial"].str.split(" ").str[0].unique():                 # B (trial = first word, cohorts of FIGHT-202 together)
        tr = em[~em["trial"].str.startswith(trial)]
        k = int(np.argmin(sum((mc[a] - o) ** 2 for a, o in zip(tr.index, tr["orr"]))))
        for key in em.index[em["trial"].str.startswith(trial)]:
            P_.append(pred(key, k, "B leave-one-trial-out global tau", {"naive": tr["orr"].mean()}))
    for key in em.index:                                                     # C
        same = em[(em["class"] == em.loc[key, "class"]) & ~em["trial"].str.startswith(em.loc[key, "trial"].split(" ")[0])]
        if len(same):
            k = int(np.argmin(sum((mc[a] - o) ** 2 for a, o in zip(same.index, same["orr"]))))
            P_.append(pred(key, k, "C same-class transfer", {"naive": same["orr"].mean()}))
    for key, ctl in CONTROL.items():                                         # D
        if key in mc and ctl in mc:
            k = int(np.argmin(np.abs(mc[ctl] - AR.loc[ctl, "orr"])))
            P_.append(pred(key, k, "D control-arm anchor", {"naive": AR.loc[ctl, "orr"]}))
    # null for mode B: each arm keeps its pool and synthetic draws but gets the DCNA of randomly chosen drug(s)
    # (same number of drugs) from the mapped set; the leave-one-trial-out fit is repeated
    def curve(key, drugs):
        pidx, idx, _ = draws[key]
        V = dc.loc[drugs, pidx].values.max(0)
        return (V[idx][:, :, None] > taus[None, None, :]).mean(1).mean(0)
    allds = list(dc.index)
    bm = [d for d in P_ if d["mode"].startswith("B")]
    obs_r = stats.pearsonr([d["pred"] for d in bm], [d["orr"] for d in bm])[0]
    null_r = []
    for _ in range(200):
        mc0 = {k: curve(k, list(rng.choice(allds, draws[k][2], replace=False))) for k in em.index}
        pr_, ob_ = [], []
        for trial in em["trial"].str.split(" ").str[0].unique():
            tr = em[~em["trial"].str.startswith(trial)]
            k = int(np.argmin(sum((mc0[a] - o) ** 2 for a, o in zip(tr.index, tr["orr"]))))
            for key in em.index[em["trial"].str.startswith(trial)]:
                pr_.append(mc0[key][k]); ob_.append(em.loc[key, "orr"])
        null_r.append(stats.pearsonr(pr_, ob_)[0] if np.std(pr_) > 0 else 0)
    log.info("Mode B: observed r %.2f; random-drug null mean %.2f, 95th pct %.2f, P %.3f", obs_r, np.mean(null_r), np.percentile(null_r, 95),
             (1 + np.sum(np.array(null_r) >= obs_r)) / 201)
    PR = pd.DataFrame(P_)
    ci = PR.apply(lambda r: stats.binomtest(int(round(r["orr"] * r["n"])), int(r["n"])).proportion_ci(), axis=1)
    PR["orr_lo"], PR["orr_hi"] = [c.low for c in ci], [c.high for c in ci]
    PR["covered"] = (PR["orr"] >= PR["lo"]) & (PR["orr"] <= PR["hi"])
    PR.to_csv(os.path.join(outdir, f"emulation_predictions{sfx}.tsv"), sep="\t", index=False, float_format="%.4g")
    S = []
    for mode, g in PR.groupby("mode"):
        S.append({"mode": mode, "arms": len(g), "pearson": stats.pearsonr(g["pred"], g["orr"])[0] if len(g) > 2 and g["pred"].std() > 0 else np.nan,
                  "spearman": stats.spearmanr(g["pred"], g["orr"])[0] if len(g) > 2 else np.nan, "mae": (g["pred"] - g["orr"]).abs().mean(),
                  "naive_mae": (g["naive"] - g["orr"]).abs().mean() if "naive" in g and g["naive"].notna().any() else np.nan,
                  "coverage": g["covered"].mean(),
                  "null_pearson_95": np.percentile(null_r, 95) if mode.startswith("B") else np.nan,
                  "null_p": (1 + np.sum(np.array(null_r) >= obs_r)) / 201 if mode.startswith("B") else np.nan})
    S = pd.DataFrame(S)
    S.to_csv(os.path.join(outdir, f"emulation_summary{sfx}.tsv"), sep="\t", index=False, float_format="%.4g")
    with pd.option_context("display.width", 250, "display.max_rows", 100):
        log.info("Arms:\n%s", AR.round(3).to_string())
        log.info("Predictions:\n%s", PR[["mode", "trial", "drugs", "pool", "orr", "pred", "lo", "hi", "tau", "covered"]].round(3).to_string(index=False))
        log.info("Summary:\n%s", S.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
