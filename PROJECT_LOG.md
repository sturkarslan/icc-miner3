# ICC MINER project log

Project memory for the intrahepatic cholangiocarcinoma (ICC / iCCA) regulatory-network model. Same pipeline as
the HCC project (`/proj/omics4tb2/sturkarslan/HCC`, GitHub `sturkarslan/hcc-miner3`); ICC is a separate model and
is never mixed into the HCC network. Newest entries first. Everything is written inside
`/proj/omics4tb2/sturkarslan/ICC`.

## Open questions

- **ICC classifier gene lists** (Sia 2013, Dong 2022 S1–S4, STIM five classes, Job 2020 + recommended additions; see
  the 2026-10-02 classifier-panel entry) are still to extract. Run `scripts/tools/fetch_signature_sources.py` on the
  login node and push `docs/signature_sources_inventory.md` (or open the Cloud network to PMC / publishers); then
  one extraction script per paper fills `config/subtype_signatures_custom.tsv`, then `config/reference_panel.yaml`
  for ICC and 07c / 07d / 09.
- **GC-rich chromosome arms look unreliable in the FU-iCCA copy-number table** (17p/q, 19p/q, 22q; see step 03b entry).
  Decide at step 05 whether to drop them or correct for a per-sample GC component.
- NODE cohorts OEP002768 (validation) and OEP002560 (multi-region) are still not downloaded.
- External survival validation beyond GSE244807 / TCGA-CHOL / GSE107943: the array cohorts (GSE89749, GSE26566,
  GSE32225, GSE76297) have no survival in GEO.
- With one discovery cohort there is no cohort-consistency filter for causal flows and no cross-cohort risk training
  as in HCC; replacements (split-half / bootstrap stability, validation-cohort replication) to be set at steps 05–06.

## Decisions

- **[2026-10-02] ICC classifier panel reviewed; sources registered (`config/signature_sources.yaml`).** Claude Cloud
  could not extract the gene lists this time: the Cloud environment's network policy blocks PMC, Europe PMC, NCBI,
  HAL and the publisher sites (only GitHub is reachable). New `scripts/tools/fetch_signature_sources.py` resolves
  each paper (NCBI ID converter, title logged), downloads the supplements (Europe PMC zip → PMC page → Elsevier
  mmc via Crossref PII) into `data/papers/<key>/`, and writes `docs/signature_sources_inventory.md` (sheets, first
  rows, gene-symbol-like columns; FU-iCCA `manual/` tables included for the Dong subgroup labels).
  - **"Beaufrère five classes" are the STIM classes of Martin-Serrano et al., Gut 2023** (immune classical, inflammatory
    stroma; hepatic stem-like, tumour classical, desert-like). The gene lists come from Martin-Serrano; Beaufrère et al.
    (JHEP Reports 2025, PMC12800354) assigned them to GSE244807 (hepatic stem-like 90 / 246), so their per-sample
    labels are a check of our STIM calls in GSE244807, as Andersen was for GSE107943. The PMID 39242455 given for
    GSE244807 in the cohort table was not confirmed.
  - Panel (priority 1 = requested): Sia 2013 Proliferation / Inflammation (+ GSE32225 labels); STIM five classes;
    Job 2020 I1–I4 (14 TME signatures); Dong 2022 S1–S4 (per-patient labels for FU-iCCA, our discovery cohort, so
    compared directly; protein markers). Priority 2: Chaisaingmongkol 2017 TIGER-LC C1 / C2 (shared HCC / iCCA;
    GSE76297 is on the server); Fan 2024 Nat Commun two CCA subtypes (30-gene classifier, CORE-37 prognostic);
    Song 2022 large-duct (S100P) vs small-duct (SPP1), needed because our risk score follows that axis.
    Priority 3: Lin 2026 Cell Rep Med LIHV 1,341-gene set / five subtypes (multi-region).
    Kept from MSigDB: Andersen 2012, Oishi 2012. Not used as expression templates: Nakamura 2015, Jusakul 2017
    (genomic / methylation clusters), Farshidfar 2017 (IDH is a driver feature), Montal 2020 (extrahepatic).
  - Fallback if a supplement has no gene list: derive class templates from the authors' labels (GSE32225 for Sia,
    FU-iCCA for Dong, GSE244807 for STIM) and say so in the set's reference column.

- **[2026-10-02] GitHub: `sturkarslan/icc-miner3` created by the user; `main` pushed.** Claude Cloud will supply the ICC
  classifier / subtype gene lists (Sia 2013, Dong 2022, Beaufrère 2024, Job 2020 …); 07c, 07d, the head-to-head and
  the publication figures wait for that panel.
- **[2026-10-02] Step 08c: response test, GSE255058 (18 pre-treatment biopsies, 9 responders): negative.** Risk score AUC
  0.47 (p 0.86). No program differs at nominal p < 0.05 (0 of 164; 8 expected by chance). Closest: P105 and P103
  (AUC 0.78, p 0.052); P105 is the program that overlaps the nivolumab-responder / immune signature. Underpowered;
  report as no evidence.
- **[2026-10-02] Step 08b replaced by split-half stability** (`08b_loco.py` adapted; matrices keep the name `loco_no<H>`
  with H = half A or B; outputs in `results/08_validation/split/`). Halves are stratified by cohort (seed 12). Each
  half-network: ComBat → MINER → technical filter → programs → causal. Compared with the full network: regulators,
  regulon Jaccard, program activity in the held-out half, driver → regulator edges, and risk (ridge trained on FU-iCCA
  patients of the kept half, tested on FU-iCCA patients of the held-out half). SLURM 15057–15067.
  Expect lower high-confidence causal recovery by design: each half has about half the altered tumours, so few
  features reach 25 altered.

- **[2026-10-02] Step 07a/07b: signature library and class mapping (first pass, MSigDB + the HCC custom immune sets).**
  - `config/subtype_signatures.yaml` rewritten for ICC: library = cholangiocarcinoma, liver-cancer and pancreatic-cancer
    C2 sets + hallmarks + custom (242 sets); NTP classifiers Andersen 2012 (class 1 / class 2), Hoshida S1–S3,
    Oishi 2012 stem-like / mature, Montironi 20-gene Inflamed. **Missing (gene lists not on the server):** Sia 2013
    proliferation / inflammation, Dong 2022 S1–S4, Beaufrère 2024 five classes, Job 2020 microenvironment classes.
  - **Check against authors' labels:** Andersen NTP call vs GSE107943 authors' class A/B: ARI 0.84 (25 assigned tumours).
  - **Risk score follows the known large-duct / small-duct axis.** Median risk z: Andersen class 2 +1.05 vs class 1 −0.69
    (KW p 2e-35); Oishi mature +0.81 vs stem-like −0.68 (1e-33); Hoshida S1 +0.67, S3 −0.51 (1e-12); inflamed vs not: weak
    (p 0.04). By driver: KRAS-mutant +1.46 vs −0.29 wild type (p 2e-12); TP53 +0.29 vs −0.21 (0.006); BAP1 −0.44 vs −0.07
    (0.011); FGFR2 fusion −0.40 vs −0.13 (0.054); IDH ≈ no difference.
  - **Largest risk weights:** adverse = programs matching Andersen class 2 (P133, r 0.97; JUN / FOSL1 / BACH1 regulons),
    pancreatic-ductal-adenocarcinoma-like (P5, r 0.81), hypoxia (P35), proliferative G3-like (P138), mitotic spindle (P137);
    protective = Andersen class 1 programs (P37 r 0.93, P49 0.82) and the Oishi stem-like program (P83, r 0.96).
    So, as in HCC, the risk model mostly recovers an established prognostic axis; whether it adds to Andersen class
    is the head-to-head still to run.
  - 96 of 164 programs have a signature overlap at FDR < 0.05; median best |r| with a signature 0.70.
  - Not yet adapted: 07c (integrated figures, beyond-known test, head-to-head), 07d (causal flow figures), 07e/07f
    equivalents, 08b (LOCO → split-half), 09 (publication figures), `reference_panel.yaml` for ICC.

- **[2026-10-02] Steps 06 and 08: risk model and first external validation.**
  - **Prognostic units (FU-iCCA OS, 36 months; 244 patients, 94 deaths):** 1,827 of 3,572 regulons and 93 of 164 programs at
    q ≤ 0.1 in FU-iCCA alone; with the same sign in TCGA and GSE107943: 1,402 regulons (1,182 adverse), 67 programs
    (59 adverse). The two small cohorts have no significant unit on their own (12 and 14 events).
  - **Ridge on 164 program activities, trained in FU-iCCA (primary model, as in HCC):** in-sample C 0.75 (optimistic).
    TCGA-CHOL: C 0.58, HR/SD 1.95 (0.88–4.31), p 0.10. GSE107943: C 0.68, HR/SD 2.27 (1.22–4.21), p 0.010; stage-adjusted 2.48.
    Both cohorts were in the (unsupervised) network but not in risk training. Ridge on regulons is similar (0.61 / 0.68).
    MINER xgboost: GSE107943 C 0.77, TCGA 0.53 (unstable with 30 samples).
  - **External, GSE244807 (step 08 rewritten for ICC; `hcc_08_external_validation.py` keeps the HCC version):**
    all 3,572 regulons scored. Overall C 0.65, HR/SD 1.67 (1.38–2.02), p 1e-7, top 20% HR 2.98, **but the risk score
    correlates r 0.75 with genes detected in this cohort**, and specimen type is tied to both, so the overall figure is
    inflated. Honest estimates: Cox stratified by specimen HR/SD 1.32 (p 0.025); also adjusted for genes detected 1.73
    (p 2e-4); surgical specimens only (n 103, 42 deaths) C 0.62, HR/SD 1.50 (1.06–2.13), p 0.022; biopsies only
    (n 127, 95 deaths) C 0.57, HR/SD 1.14, p 0.27. **Reading: the model transfers to resected tumours (the population it
    was trained on) with a modest effect, and not convincingly to biopsies of unresectable disease.**
  - Still to do: ICC signature panel and subtype mapping (step 07), head-to-head against published ICC classifiers,
    split-half stability of network / causal flows, GSE255058 response test, GSE32225 class check, figures (step 09).

- **[2026-10-02] Steps 04–05 on the 315-tumour network.**
  - **MINER (04):** 4,029 regulons, 405 regulators, 9,414 regulon genes, 202 programs, 16 states (45 min).
    FU-iCCA-only sensitivity run: 5,031 regulons, 444 regulators, 221 programs, 18 states.
  - **Technical modules (04b, new `04b_technical_modules.py`):** module 0 (625 genes; SRRM2, SAFB2, ACIN1, KMT2A, many ZNFs:
    long nuclear-retained transcripts, no marker biology) tracks genes detected (r 0.56 in FU-iCCA) and is not associated
    with survival (Cox HR/SD 0.96, p 0.70) or stage (p 0.16). Rule: modules with r ≥ 0.7 to module 0 in FU-iCCA and
    |marker r| < 0.5 → 95 of 901 modules (2,303 genes). Same treatment as HCC modules 1/2/4/6: expression unchanged,
    regulons mostly in these modules dropped.
  - **Filtered network (04c):** 457 regulons dropped (11%; HCC 4%) → **3,572 regulons, 398 regulators, 164 programs, 19 states.**
  - **Copy-number arms dropped before causal inference:** 16p, 17p, 17q, 19p, 19q, 22q, 11q (GC-wave artefact: mean r ≥ 0.45
    with each other across samples, gains and losses both frequent). 6p gain (47%) loads on the same component (r 0.39)
    and is kept but should be read with caution. 78 features go to step 05.
  - **Causal inference (05):** `min_cohorts: 1` (genomics is essentially FU-iCCA), `min_altered_hc: 25` (keeps the FGFR2
    fusion, n 28). 20,722 MINER flows → **6,205 high-confidence** (q ≤ 0.1 both tests, |d| ≥ 0.5, ≥ 25 altered), 4,672 also
    significant after adjustment, 73 cis-dosage; 1,299 regulon families. High-confidence families per driver: KRAS 202,
    BAP1 163, TP53 124, IDH pathway 96, IDH1 80, FGFR2 fusion 68, ARID1A ~2; arms: 16q loss 296, 14q loss 197, 2q gain 174,
    13q loss 171, 1q gain 139, 3p loss 131. Plausibility: KRAS raises FOSL1 / STAT3 / HOX regulons; TP53 raises E2F1.
    No cross-cohort consistency filter is possible, so these are less stringent than the HCC flows; a split-half
    stability check is still to do.
  - **Risk (06) submitted:** SLURM 15053 (train FU-iCCA OS; in-network tests TCGA, GSE107943).

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
