#!/usr/bin/env python
"""Step 08e (ICC): do the high-confidence causal flows replicate in an independent cohort with genomics?

OEP002768 (unique patients; never in the network): driver calls from the paper's 24-gene driver table (WES) and RNA-seq
FGFR2 fusions. For each discovery driver with >= min_altered altered and wild-type tumours there:
  - regulon level: one regulon per (driver, regulon family) from highConfidenceCausalResults.csv, scored in OEP002768
    as the mean z of its genes; predicted direction = sign of the discovery Cohen's d. Welch t, altered vs wild type.
  - regulator level: regulator mRNA (z), predicted direction = sign of MutationRegulatorEdge.
Replication = same sign; also p < 0.05 in the same direction. Null: the same number of random regulons (not causally
linked to the driver) with the same predicted signs, n_perm draws -> empirical p for the sign-agreement rate.

Output: results/08_validation/OEP002768/causal_replication.tsv (per driver) and causal_replication_flows.tsv
"""

import importlib.util
import json
import os

import numpy as np
import pandas as pd
from scipy import stats

from hcc_common import load_params, miner_id_backmap, p, setup_logging

MAP = {"MUT_TP53": "mut_TP53", "MUT_KRAS": "mut_KRAS", "MUT_IDH1": "mut_IDH1", "MUT_IDH2": "mut_IDH2", "MUT_BAP1": "mut_BAP1",
       "MUT_ARID1A": "mut_ARID1A", "MUT_ARID2": "mut_ARID2", "MUT_PBRM1": "mut_PBRM1", "FUS_FGFR2": "fusion_FGFR2",
       "PATH_IDH": ["mut_IDH1", "mut_IDH2"]}


def main():
    P = load_params(None)
    res = p(P["paths"]["results"])
    mx = P["miner"]["matrix"]
    outdir = os.path.join(res, "08_validation", "OEP002768")
    log = setup_logging(outdir, "08e_causal_replication")
    spec = importlib.util.spec_from_file_location("s08", os.path.join(os.path.dirname(os.path.abspath(__file__)), "08_external_validation.py"))
    s08 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(s08)
    cfg = dict(P["validation"]["cohorts"]["OEP002768"], _name="OEP002768", _res=res)
    x, clin = s08.LOADERS[cfg["loader"]](cfg, log)
    genes = pd.read_csv(os.path.join(res, "01_harmonized", "genes.tsv"), sep="\t", index_col=0)
    x = x.loc[x.index.intersection(genes.index[genes["kept"]])]
    z = s08.zrows(x).dropna(how="all")
    back = miner_id_backmap(p(P["miner"]["idmap"]), genes.index)
    regs = {k: [back.get(g, g) for g in v] for k, v in json.load(open(os.path.join(res, "04_miner", mx, "mechinf", "regulons_filtered.json"))).items()}
    score = {k: z.loc[[g for g in v if g in z.index]].mean() for k, v in regs.items() if sum(g in z.index for g in v) >= max(3, 0.5 * len(v))}
    score = pd.DataFrame(score)
    hc = pd.read_csv(os.path.join(res, "05_causal", mx, "highConfidenceCausalResults.csv"), index_col=0)
    hc["Regulon_ID"] = hc["Regulon_ID"].astype(str)
    hc = hc.assign(ad=hc["cohen_d"].abs()).sort_values("ad", ascending=False).drop_duplicates(["Mutation", "family"])
    sym2ens = genes.reset_index().drop_duplicates("symbol").set_index("symbol")["ensembl"]
    rng = np.random.default_rng(1)
    rows, flows = [], []
    for drv, col in MAP.items():
        if drv not in set(hc["Mutation"]):
            continue
        cols = col if isinstance(col, list) else [col]
        prof = clin[cols].notna().all(axis=1)
        alt = (clin.loc[prof, cols].fillna(0).astype(float).max(axis=1) == 1)
        a, w = alt.index[alt], alt.index[~alt]
        a, w = [s for s in a if s in score.index], [s for s in w if s in score.index]
        if len(a) < P["validation"].get("causal_min_altered", 5) or len(w) < 5:
            log.info("%s: %d altered / %d wild type in OEP002768: not testable", drv, len(a), len(w))
            continue
        f = hc[(hc["Mutation"] == drv) & hc["Regulon_ID"].isin(score.columns)]
        t, pv = stats.ttest_ind(score.loc[a, f["Regulon_ID"]], score.loc[w, f["Regulon_ID"]], equal_var=False)
        pred = np.sign(f["cohen_d"].values)
        agree = np.sign(t) == pred
        sig = agree & (pv < 0.05)
        # regulator mRNA
        rr = f.drop_duplicates("regulator_symbol")
        re_ = [(sym2ens.get(r), e) for r, e in zip(rr["regulator_symbol"], rr["MutationRegulatorEdge"]) if sym2ens.get(r) in z.index]
        tr, _ = stats.ttest_ind(z.loc[[g for g, _ in re_], a].T, z.loc[[g for g, _ in re_], w].T, equal_var=False) if re_ else ([], [])
        ragree = float(np.mean(np.sign(tr) == np.sign([e for _, e in re_]))) if re_ else np.nan
        # null: random regulons not linked to this driver, same predicted signs
        other = [r for r in score.columns if r not in set(hc.loc[hc["Mutation"] == drv, "Regulon_ID"])]
        tall, _ = stats.ttest_ind(score.loc[a, other], score.loc[w, other], equal_var=False)
        tall = pd.Series(tall, index=other)
        null = [np.mean(np.sign(tall[rng.choice(other, len(f), replace=False)].values) == pred) for _ in range(1000)]
        pe = (1 + np.sum(np.array(null) >= agree.mean())) / 1001
        rows.append({"driver": drv, "n_altered": len(a), "n_wildtype": len(w), "flows_tested": len(f), "sign_agreement": agree.mean(),
                     "same_sign_p_lt_0_05": sig.mean(), "null_sign_agreement_mean": float(np.mean(null)), "empirical_p": pe,
                     "regulators_tested": len(re_), "regulator_sign_agreement": ragree})
        flows.append(f.assign(oep_t=t, oep_p=pv, replicated=agree)[["Mutation", "regulator_symbol", "Regulon_ID", "family", "program",
                                                                     "cohen_d", "oep_t", "oep_p", "replicated"]])
        log.info("%s: %d altered vs %d; %d flows: same sign %.0f%% (null %.0f%%, p %.3f), same sign and p<0.05 %.0f%%; regulators %d, "
                 "same sign %.0f%%", drv, len(a), len(w), len(f), 100 * agree.mean(), 100 * np.mean(null), pe, 100 * sig.mean(),
                 len(re_), 100 * ragree if re_ else np.nan)
    pd.DataFrame(rows).to_csv(os.path.join(outdir, "causal_replication.tsv"), sep="\t", index=False, float_format="%.4g")
    if flows:
        pd.concat(flows).to_csv(os.path.join(outdir, "causal_replication_flows.tsv"), sep="\t", index=False, float_format="%.4g")


if __name__ == "__main__":
    main()
