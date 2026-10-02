#!/usr/bin/env python
"""Prepare OEP002768 (FU-CCA; Deng et al., Hepatology 2023) from the exported supplementary sheets
(data/OEP002768/tables/): one table of iCCA tumours with RNA-seq, and a TPM-ready FPKM matrix.

  samples_icca.tsv   sample (OEP<patient number>), rna_id, patient, wes_id, os_days, os_event, duct_type, stage,
                     overlap_fu (True = same patient as a FU-iCCA sample, config/oep002768_fu_icca_overlap.tsv),
                     fusion_FGFR2 (RNA-seq call), mut_<gene> for the 24 driver genes of sheet 2 (1/0; empty = no WES)
  expression_fpkm_icca.tsv   genes (symbols) x samples, FPKM as published (12,724 pre-filtered genes)
"""

import os

import numpy as np
import pandas as pd

D = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data", "OEP002768", "tables")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def main():
    cl = pd.read_csv(os.path.join(D, "1_Clinical_information.tsv"), sep="\t", dtype=str)
    ic = cl[(cl["Histology"] == "iCCA") & cl["Tumor (T) RNA-seq ID"].notna()].copy()
    e = pd.read_csv(os.path.join(D, "5_RNA_Seq_FPKM.tsv"), sep="\t", index_col=0).dropna(axis=1, how="all")
    e = e[~e.index.duplicated()]
    e.columns = [c.replace("_", "-") for c in e.columns]
    ic["rna_id"] = ic["Tumor (T) RNA-seq ID"].str.replace("_", "-")
    ic = ic[ic["rna_id"].isin(e.columns)]
    ov = pd.read_csv(os.path.join(ROOT, "config", "oep002768_fu_icca_overlap.tsv"), sep="\t")
    s = pd.DataFrame({"sample": "OEP" + ic["Patient No."].str.replace("CCA#", ""), "rna_id": ic["rna_id"], "patient": ic["Patient No."],
                      "wes_id": ic["Tumor (T) WES ID"], "os_days": pd.to_numeric(ic["Overall survival(day)"], errors="coerce").round(),
                      "os_event": ic["Survival(1,dead;0,alive)"], "duct_type": ic["iCCA classification"], "stage": ic["iccStage"],
                      "sex": ic["Gender"], "age": ic["Age"], "overlap_fu": ic["Patient No."].isin(ov["OEP002768_patient"]).values})
    fu = pd.read_csv(os.path.join(D, "11_FGFR2_kinase_fusions.tsv"), sep="\t", dtype=str)
    fus = set(fu.loc[fu["FusionName"].str.contains("FGFR2", na=False), "sample"].str.replace("_", "-"))
    s["fusion_FGFR2"] = s["rna_id"].isin(fus).astype(int)
    dr = pd.read_csv(os.path.join(D, "2_Drive_genes_signatures.tsv"), sep="\t", dtype=str).set_index("Patient No.")
    genes = list(dr.columns[1:dr.columns.get_loc("SigA(SBS30)")])
    for g in genes:
        s[f"mut_{g}"] = [np.nan if pt not in dr.index else int(isinstance(dr.loc[pt, g], str) and dr.loc[pt, g].strip() != "")
                         for pt in s["patient"]]
    s.to_csv(os.path.join(D, "samples_icca.tsv"), sep="\t", index=False)
    x = e[s["rna_id"]].set_axis(s["sample"].values, axis=1)
    x.index.name = "gene"
    x.to_csv(os.path.join(D, "expression_fpkm_icca.tsv"), sep="\t")
    nd = (x / x.sum() * 1e6 >= 1).sum()
    print(f"{len(s)} iCCA tumours with RNA; overlap with FU-iCCA {int(s['overlap_fu'].sum())}; unique {int((~s['overlap_fu']).sum())}")
    print(f"unique: WES {int(s.loc[~s['overlap_fu'], 'mut_TP53'].notna().sum())}, FGFR2 fusion {int(s.loc[~s['overlap_fu'], 'fusion_FGFR2'].sum())} "
          f"(fusion IDs matched to RNA IDs: {len(fus & set(e.columns))} of {len(fus)}), genes detected < 9000: {int((nd[s.loc[~s['overlap_fu'], 'sample']] < 9000).sum())}")
    print("mutated (unique, WES):", {g: int(s.loc[~s["overlap_fu"], f"mut_{g}"].sum()) for g in ["TP53", "KRAS", "IDH1", "IDH2", "BAP1", "ARID1A", "PBRM1", "FGFR2"]})
    s["n_genes_detected"] = nd.values
    s.to_csv(os.path.join(D, "samples_icca.tsv"), sep="\t", index=False)


if __name__ == "__main__":
    main()
