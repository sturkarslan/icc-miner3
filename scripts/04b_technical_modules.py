#!/usr/bin/env python
"""Step 04b (part 2): list co-expression modules judged technical, for step 04c.

Rule (same idea as the HCC project, made explicit): take the anchor module (miner.technical.anchor_module:
the large module of long, nuclear-retained / intron-rich transcripts with no marker biology that tracks
genes detected per sample). A module is technical when, within the reference cohort, its mean-z profile
correlates >= min_r_anchor with the anchor AND it has no marker biology (|best_marker_r| from step 04b
< max_marker_r). Expression is not changed; step 04c drops regulons that sit mostly in these modules.

Output: results/04_miner/<matrix>/module_qc/technical_modules.tsv (all modules with the two statistics
and the call). Copy the printed list to miner.exclude_modules.
"""

import argparse
import json
import os

import numpy as np
import pandas as pd

from hcc_common import load_params, miner_id_backmap, p, setup_logging


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--params", default=None)
    ap.add_argument("--matrix", default=None)
    args = ap.parse_args()
    P = load_params(args.params)
    M, T = P["miner"], P["miner"]["technical"]
    matrix = args.matrix or M["matrix"]
    res = p(P["paths"]["results"])
    mdir = os.path.join(res, "04_miner", matrix)
    log = setup_logging(os.path.join(mdir, "module_qc"), "04b_technical_modules")
    z = pd.read_csv(os.path.join(res, "02_batch_corrected", f"expression_{matrix}_z.csv"), index_col=0)
    S = pd.read_csv(os.path.join(res, "01_harmonized", "samples.tsv"), sep="\t", index_col=0)
    st = pd.read_csv(os.path.join(res, "01_harmonized", "sample_stats.tsv"), sep="\t", index_col=0)
    back = miner_id_backmap(p(M["idmap"]), z.index)
    mods = json.load(open(os.path.join(mdir, "coexpr", "coexpressionDictionary.json")))
    q = pd.read_csv(os.path.join(mdir, "module_qc", "modules.tsv"), sep="\t", index_col=0)
    ref = [s for s in S.index[S["cohort"] == T["reference_cohort"]] if s in z.columns]
    nd = st.loc[ref, "n_genes_detected"]
    E = pd.DataFrame({int(k): z.loc[[g for g in (back.get(x, x) for x in v) if g in z.index], ref].mean()
                      for k, v in mods.items()}).T
    out = q[["n_genes", "n_regulons", "best_marker_program", "best_marker_r", "top_genes"]].copy()
    out["r_genes_detected"] = E.apply(lambda v: np.corrcoef(v, nd)[0, 1], axis=1)
    if T.get("anchor_module") is None and T.get("anchor_genes"):
        # gene-based anchor transferred from the main design: the module sharing most genes with the anchor gene list
        ag = {l.strip() for l in open(p(T["anchor_genes"])) if l.strip() and not l.startswith("#")}
        sym = pd.read_csv(os.path.join(res, "01_harmonized", "genes.tsv"), sep="\t", index_col=0)["symbol"]
        ov = pd.Series({int(k): len({sym.get(back.get(x, x), "") for x in v} & ag) / len(ag) for k, v in mods.items()})
        T["anchor_module"] = int(ov.idxmax())
        log.info("Anchor from %s (%d genes): module %d holds %.0f%% of them (%d genes, r %.2f with genes detected); top genes %s",
                 T["anchor_genes"], len(ag), T["anchor_module"], 100 * ov.max(), out.loc[T["anchor_module"], "n_genes"],
                 out.loc[T["anchor_module"], "r_genes_detected"], out.loc[T["anchor_module"], "top_genes"])
    if T.get("anchor_module") is None:
        # automatic anchor: among large modules (>= anchor_min_genes) without marker biology, the one that tracks
        # genes detected most closely. Check the logged top genes (expected: long nuclear-retained transcripts).
        c = out[(out["n_genes"] >= T.get("anchor_min_genes", 100)) & (out["best_marker_r"].abs() < T["max_marker_r"])]
        T["anchor_module"] = int(c["r_genes_detected"].idxmax())
        log.info("Automatic anchor: module %d (%d genes, r %.2f with genes detected); top genes %s", T["anchor_module"],
                 c.loc[T["anchor_module"], "n_genes"], c.loc[T["anchor_module"], "r_genes_detected"], c.loc[T["anchor_module"], "top_genes"])
    anchor = E.loc[int(T["anchor_module"])]
    out["r_anchor"] = E.apply(lambda v: np.corrcoef(v, anchor)[0, 1], axis=1)
    out["technical"] = (out["r_anchor"] >= T["min_r_anchor"]) & (out["best_marker_r"].abs() < T["max_marker_r"])
    out.to_csv(os.path.join(mdir, "module_qc", "technical_modules.tsv"), sep="\t", float_format="%.3f")
    t = out[out["technical"]]
    log.info("Anchor module %s: %d genes, r with genes detected %.2f (%s)", T["anchor_module"], out.loc[int(T["anchor_module"]), "n_genes"],
             out.loc[int(T["anchor_module"]), "r_genes_detected"], T["reference_cohort"])
    log.info("Technical modules: %d of %d (%d genes); regulons mainly in them: %d of %d", len(t), len(out), t["n_genes"].sum(),
             t["n_regulons"].sum(), out["n_regulons"].sum())
    log.info("exclude_modules: %s", sorted(t.index.tolist()))


if __name__ == "__main__":
    main()
