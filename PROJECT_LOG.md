# ICC MINER project log

Project memory for the intrahepatic cholangiocarcinoma (ICC / iCCA) regulatory-network model. Same pipeline as
the HCC project (`/proj/omics4tb2/sturkarslan/HCC`, GitHub `sturkarslan/hcc-miner3`); ICC is a separate model and
is never mixed into the HCC network. Newest entries first. Everything is written inside
`/proj/omics4tb2/sturkarslan/ICC`.

## Open questions

- **GitHub repository not created yet.** The server has no `gh` CLI or API token (SSH key only), so the repo cannot be
  created from here. Once an empty `sturkarslan/icc-miner3` exists, `git push -u origin main` publishes it (remote is set).
- **GC-rich chromosome arms look unreliable in the FU-iCCA copy-number table** (17p/q, 19p/q, 22q; see step 03b entry).
  Decide at step 05 whether to drop them or correct for a per-sample GC component.
- NODE cohorts OEP002768 (validation) and OEP002560 (multi-region) are still not downloaded.
- External survival validation beyond GSE244807 / TCGA-CHOL / GSE107943: the array cohorts (GSE89749, GSE26566,
  GSE32225, GSE76297) have no survival in GEO.
- With one discovery cohort there is no cohort-consistency filter for causal flows and no cross-cohort risk training
  as in HCC; replacements (split-half / bootstrap stability, validation-cohort replication) to be set at steps 05–06.

## Decisions

- **[2026-10-02] Discovery design changed to 315 tumours: FU-iCCA 255 + TCGA-CHOL intrahepatic 30 + GSE107943 30 (user decision).**
  GSE244807 stays held out for validation. Reasons for adding the two small cohorts: with 15–17 deaths each they are
  weak validation sets, they add non-Chinese-single-centre diversity, and 255 is small for MINER. Reasons for holding out
  GSE244807: within-cohort technical axis (PC1 53% of variance, r −0.92 with genes detected; biopsy vs surgical) and it is
  the only large independent survival cohort (181 deaths). Option not taken: add its 109 surgical specimens (≈ 424).
  - **Step 01:** 315 samples, 13,782 genes. **Step 02:** ComBat by cohort, silhouette 0.46 → −0.01, kNN mixing 0.005 → 0.79,
    within-cohort structure ρ 1.00 / 1.00 / 1.00. `miner.matrix: combat`.
  - **Step 03:** now config-driven per cohort and endpoint. OS: FU-iCCA 244 (99 deaths), TCGA 30 (15), GSE107943 30 (17);
    RFS: GSE107943 only (21 events).
  - **Step 03b:** TCGA gene and pathway mutations added (Xena GDC MAF); 92 features kept. TCGA contributes little: BAP1 6,
    PBRM1 6, IDH1 4, ARID1A 4, TP53 1, KRAS 1. Copy number and fusions are FU-iCCA only; GSE107943 has no genomics.
    Two TCGA samples are hypermutated (916 and 771 calls; ZH-A8Y7, W5-AA39): watch for passenger hits in driver features.
  - **MINER:** 315-tumour run SLURM 15047 (`results/04_miner/combat`). The FU-iCCA-only run (SLURM 15041,
    `results/04_miner/single`, 15,380 genes) is kept as a sensitivity comparison.

- **[2026-10-01] Discovery design: FU-iCCA only; GSE244807 is validation (user decision).** TCGA-CHOL (30) and GSE107943
  (30) are also kept out of the network so that every cohort with survival other than FU-iCCA is an independent test.
  One discovery cohort means no batch correction: step 02 writes `expression_single_z.csv` (`miner.matrix: single`).
  - **FU-iCCA files** are the paper's supplementary tables, placed by the user in `data/FU_iCCA/manual/` (mmc2 = Table S1,
    mmc3 = Table S2, mmc5 = Table S4) and exported sheet by sheet to `data/FU_iCCA/tables/`: clinical (262 patients),
    WES mutations (253), mRNA log2(TPM+1) (255, gene symbols), gene-level copy ratio (253), GISTIC peaks, FGFR2 fusions.
    Proteome (214) and phosphoproteome are also there (not used yet; candidates for protein-level validation).
  - **Step 01:** 255 tumours, 15,380 genes (TPM ≥ 1 in ≥ 20%). Symbols mapped to Ensembl by the HCC tiers (429 of 20,173
    unmapped). Genes detected per sample 12,901–19,569 (compare GSE244807: 3,769–29,082).
  - **Step 03 (rewritten for ICC):** OS only. 244 of 255 with OS, 99 deaths (94 within 36 months), median follow-up of
    censored patients 834 days, max 1,806. Files `survival_FU_iCCA_OS[_h36m]_miner.csv`. No recurrence endpoint.
  - **Step 03b (rewritten for ICC):** 89 features kept (≥ 10 altered, ≥ 3%): 8 gene mutations (TP53 49, KRAS 43, IDH1 30,
    BAP1 30, ARID1A 27, PBRM1 13, IDH2 11, ARID2 10), 7 pathways (IDH 41, RAS-MAPK 56, chromatin 79, …), FGFR2 fusion 28,
    3 focal amplifications (MYC, ERBB2, CCND1/FGF19; 11–13 each), 70 arm events. Mutations are all protein-altering WES
    calls in curated iCCA drivers (no VAF filter; table minimum 0.04).
  - **Copy-number caveat:** only gene-level log2 ratios are published, so arm calls are the median over the arm's genes
    at ±0.2. Expected iCCA events are there (1q gain 43%, 6q loss 36%, 3p loss 31%, 9p / 14q loss 28%), but 6p gain 47%
    is higher than expected and the GC-rich arms 17q / 19p / 19q / 22q show both gains (37–44%) and losses and
    correlate with each other (r 0.5–0.6): probably a GC-wave artefact of exome-derived ratios. CDKN2A homozygous
    deletion does not reach 10 samples at the authors' −1.3 threshold.
  - **Step 04 (MINER) submitted:** SLURM 15041.

- **[2026-10-01] (Superseded by the discovery design above.) Steps 01–02 on the three public cohorts, which led to keeping GSE244807 out of discovery.**
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
