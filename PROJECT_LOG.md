# ICC MINER project log

Project memory for the intrahepatic cholangiocarcinoma (ICC / iCCA) regulatory-network model. Same pipeline as
the HCC project (`/proj/omics4tb2/sturkarslan/HCC`, GitHub `sturkarslan/hcc-miner3`); ICC is a separate model and
is never mixed into the HCC network. Newest entries first. Everything is written inside
`/proj/omics4tb2/sturkarslan/ICC`.

## Open questions

- **FU-iCCA (NODE OEP001105; Dong et al., Cancer Cell 2022) needs a manual download** (NODE login). It is the only
  large cohort with WES, so causal inference (step 05) cannot be done without it. Files wanted are listed in
  `data/FU_iCCA/manual/README_DOWNLOAD.txt`. Same for OEP002768 and OEP002560.
- **How to handle the technical axis in GSE244807** (see 2026-10-01 entry): options are (a) FU-iCCA as the discovery
  backbone and GSE244807 as validation only; (b) keep GSE244807 in discovery with specimen type as a ComBat batch and
  the low-complexity samples removed; (c) surgical specimens only (109).
- External survival validation: none of the array cohorts (GSE89749, GSE26566, GSE32225, GSE76297) has survival in
  GEO. Survival would have to come from paper supplements.
- No GitHub remote yet for this repository (local git only).

## Decisions

- **[2026-10-01] Steps 01–02 run on the three cohorts available now (provisional; MINER not started).**
  - Step 01: GSE244807 246, TCGA-CHOL 30 intrahepatic primaries (35 primary tumours, 5 non-intrahepatic removed via
    `config/tcga_exclude.tsv`), GSE107943 30 tumours → 306 samples, 14,479 genes (TPM ≥ 1 in ≥ 20% of every cohort).
    New in `01_harmonize_expression.py`: `rpkm_table` loader (GSE107943 RPKM rescaled to TPM) and a generic
    `sample_table` selector (filters and labels from `samples_geo.tsv`).
  - Step 02: ComBat by cohort removes the cohort effect (silhouette 0.34 → −0.04; within-cohort structure ρ 0.96–1.00).
  - **Problem: GSE244807 has a dominant technical axis.** Genes detected per sample range 3,769–29,082. Within the
    cohort PC1 explains 53% of variance and correlates r −0.92 with genes detected and −0.66 with biopsy status.
    Biopsies (137) detect a median 18,500 genes, surgical specimens (109) 12,838; 8 samples detect < 9,000. Biopsy
    patients also have worse survival (median OS 9 vs 23 months; 81% vs 64% dead), so specimen type is both a
    technical and a clinical confounder. ComBat by cohort does not remove it (specimen silhouette 0.26 → 0.25).
    A network built mainly on this cohort would be largely technical (compare the HCC "technical regulons", which
    were 4% of regulons; here the axis is the first PC). MINER is therefore on hold until the discovery design is set.

- **[2026-10-01] Data fetched with the Cloud script** (`scripts/tools/fetch_icca_cohorts.py`, registry
  `config/cohorts.yaml`, inventory `results/00_inventory/`). The server node has internet access.
  | Cohort | Samples | Expression | Survival | Genomics | Status |
  |---|---|---|---|---|---|
  | GSE244807 (Beaufrère, PMID 39242455) | 246 iCCA (137 biopsy, 109 surgical) | kallisto TPM + counts | OS months + death (181 events) | none | downloaded |
  | TCGA-CHOL | 51 cases, 39 intrahepatic; 30 intrahepatic primaries with RNA | STAR TPM | OS | mutations (WES) | downloaded |
  | GSE107943 (Ahn, PMID 30941318) | 30 tumours + 27 adjacent | RPKM + counts | OS, DFS, recurrence | none | downloaded |
  | GSE255058 | 18 pre-treatment (9 R / 9 NR) | FPKM xlsx | response labels in GEO | none | downloaded; test only |
  | FU-iCCA OEP001105 | ~255 | — | — | WES | **manual NODE download** |
  | OEP002768, OEP002560 | — | — | — | — | manual NODE download |
  | GSE32225 (Sia) | 149 iCCA | Illumina DASL | none in GEO | — | downloaded; has Proliferation (92) / Inflammation (57) class labels |
  | GSE89749, GSE26566, GSE76297 | 118 / 104 / 91 CCA | arrays | none in GEO | — | downloaded; no site or survival annotation in GEO |
  GSE244807 is 246 samples as in the planning table (not 169).

- **[2026-10-01] Project set up.** Pipeline scripts copied from HCC at commit `6977a53` + later figure commits.
  `envs/hcc-prep` and `envs/pylib-miner` are symlinks to the HCC project environments (not rebuilt);
  reference files (HGNC, MSigDB, cytobands) are symlinks to `HCC/data/reference`. HCC-specific configs
  (program labels, reference panel, subtype signatures) are not copied: ICC needs its own (Sia 2013, Andersen 2012,
  Dong 2022, Beaufrère five-class signatures), to be built at step 07.

## Environment / tooling

- Python env: `envs/hcc-prep` (symlink). MINER: conda env `miner3` (`/users/sturkars/mambaforge/envs/miner3`).
- `PYTHONUTF8=1` (server locale is ISO-8859-1). SLURM partition `active`; wrappers in `scripts/slurm/`.
- Scripts keep their HCC names (`hcc_common.py`, `hcc_panel.py`); the project root is taken from the script location.

## Issues

- Scripts for steps 03–09 are still the HCC versions and will fail on ICC cohorts until adapted (cohort names,
  survival sources, genomic features, signatures).
