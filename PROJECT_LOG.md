# ICC MINER project log

Project memory for the intrahepatic cholangiocarcinoma (ICC / iCCA) regulatory-network model. Same pipeline as
the HCC project (`/proj/omics4tb2/sturkarslan/HCC`, GitHub `sturkarslan/hcc-miner3`); ICC is a separate model and
is never mixed into the HCC network. Newest entries first. Everything is written inside
`/proj/omics4tb2/sturkarslan/ICC`.

## Open questions

- **[2026-10-05] SOC response validation and in-silico trial emulation: designs written, not run.**
  `docs/soc_response_validation_design.md` (ICC SOC, response rates, drug → network map),
  `docs/trial_emulation_design.md` (shared with HCC), arms in `config/trials.yaml` (9 arms: TOPAZ-1, KEYNOTE-966,
  FIGHT-202, FOENIX-CCA2, ClarIDHy, HERIZON-BTC-01, ROAR).
  - **Key point (needs the user's decision):** a DCNA threshold set from a trial's own ORR makes predicted = observed by
    construction. Recommended instead:
    - threshold from the other trials of the same drug class (leave-one-trial-out), or from the control arm;
    - per-trial fitting only as description.
  - **Strongest ICC test:** the FGFR2-fusion contrast. FGFR inhibitors give 37–42% ORR in fusion-positive tumours only,
    and the fusion → programs 49 / 51 / 52 / 54 flow replicates in OEP002768. Ivosidenib (ORR ~2%, cytostatic) is the
    expected-low control.
  - Small eligible pools (FGFR2 fusion 28 + 7, ERBB2 amp ~12, BRAF < 10) limit biomarker-trial emulation.
  - **Next:**
    - `fetch_drug_targets.py` (ChEMBL) and `fetch_trials.py` (ClinicalTrials.gov v2; blocked from Cloud, run on the
      server);
    - fill the trial Table 1 fractions;
    - then step 10 (10a DCNA, 10b emulation, 10c figures).

- **ICC classifiers are extracted** (see 2026-10-02 extraction entry). Still open: (1) the original Martin-Serrano Gut
  online Table S5 to confirm the STIM gene-to-class blocks (taken from Lin 2026; put the file in
  `data/papers/martin_serrano2023/manual/`); (2) run 07a / 07b on the server with the new classifiers and published
  labels, then `config/reference_panel.yaml` for ICC and 07c / 07d / 09; (3) the Sia template transfers poorly to
  RNA-seq (below): decide whether to keep it as an NTP classifier or only as a library set.
- **GSE89749 survival**: Song 2022 Suppl Data 4 gives survival days and site (intrahepatic) for 115 GSE89749 samples
  but no vital status; Jusakul 2017 (Cancer Discov) Table S1 should have both (aacrjournals.org not reachable from
  Cloud). With status this would be a second external survival cohort.
- **GC-rich chromosome arms look unreliable in the FU-iCCA copy-number table** (17p/q, 19p/q, 22q; see step 03b entry).
  Decide at step 05 whether to drop them or correct for a per-sample GC component.
- NODE cohorts OEP002768 (validation) and OEP002560 (multi-region) are still not downloaded.
- External survival validation beyond GSE244807 / TCGA-CHOL / GSE107943: the array cohorts (GSE89749, GSE26566,
  GSE32225, GSE76297) have no survival in GEO.
- With one discovery cohort there is no cohort-consistency filter for causal flows and no cross-cohort risk training
  as in HCC; replacements (split-half / bootstrap stability, validation-cohort replication) to be set at steps 05–06.

## Decisions

- **[2026-10-05] Split-half stability on d374 (SLURM 15129–15139), Figure 2g filled.** Halves A / B held out: regulators
  recovered 96% / 96%; program activity r in the held-out half 0.80 / 0.80 (risk-weighted programs 0.82 / 0.83); regulon
  membership median best Jaccard 0.10 / 0.11; full-network causal edges among half-network flows 46% / 39% (high-confidence
  23% / 22%; by driver KRAS 43 / 40%, TP53 26 / 49%, IDH 34 / 40%, BAP1 46 / 52%, FGFR2 fusion 51 / 4% — about 14 fusions per
  half); risk in the unseen FU-iCCA half C 0.69 / 0.75, HR/SD 2.05 / 2.35. Essentially the same as on d315. The FGFR2-fusion
  edges are unstable at half size but replicate in direction in OEP002768 (97%, step 08e).

- **[2026-10-05] ICC publication figures (step 09 adapted) and legends.** `config/reference_panel.yaml` rewritten for ICC
  (blocks: large-duct / aggressive, small-duct / differentiated, immune / stromal; signatures; classes = our NTP calls for
  STIM, Dong 2022, Song duct, Andersen, Lin 2026; Sia 2013 left out). `config/program_labels.tsv` curated for the 40
  programs with the largest weights + the 4 FGFR2-fusion target programs (IDs refer to the d374 network).
  Figure 1: design, numbers, programs × states with class / driver tracks, program–signature r, FGFR2-fusion causal flow,
  causal replication in OEP002768 (replaces the HCC driver panels). Figure 2: weights, risk by class, states by risk with
  GuanRank (ρ 0.73, P 2.8e-4, 20 states), KM in five test settings, forest (pooled held-out HR/SD 1.62, 1.27–2.05),
  head-to-head (07g), split-half (pending). Legends in `docs/figure_legends.md`.
  - Correction to the d374 / d315 / d433 comparison table: the TCGA / GSE107943 C-indices were from the regulon ridge model;
    program ridge values are now in the table (`08d_compare_designs.py` fixed). Conclusions unchanged.

- **[2026-10-04] Causal flows replicate in an independent cohort (step 08e, OEP002768: 59 unique patients, WES driver
  table, never in the network).** One regulon per driver × family from the high-confidence flows, scored in OEP002768
  (mean z), altered vs wild type; null = random non-linked regulons with the same predicted signs (1,000 draws).
  | driver | altered / WT | flows | same direction | null | p | same dir. and p < 0.05 | regulator mRNA same dir. |
  |---|---|---|---|---|---|---|---|
  | TP53 | 10 / 44 | 124 | 97% | 52% | 0.001 | 29% | 86% |
  | BAP1 | 8 / 46 | 142 | 96% | 49% | 0.001 | 30% | 67% |
  | FGFR2 fusion | 7 / 52 | 94 | 97% | 52% | 0.001 | 21% | 89% |
  | IDH pathway | 11 / 43 | 68 | 76% | 42% | 0.001 | 13% | 64% |
  | IDH1 alone | 8 / 46 | 48 | 44% | 35% | 0.09 | 4% | 54% |
  KRAS not testable (3 mutants). With 7–11 altered tumours single flows rarely reach p < 0.05, but the direction of the
  causal effects replicates almost perfectly for TP53, BAP1 and FGFR2 fusion. This is stronger evidence than the
  split-half edge recovery (which re-runs the whole inference on half the data). IDH1 flows do not replicate on their own.
- **[2026-10-04] Split-half stability submitted on d374** (SLURM 15129–15139).

- **[2026-10-02] Main configuration = design d374 (user decision).** `config/params.yaml` now has GSE179443 in discovery,
  `exclude_modules: []` + gene-based technical anchor; identical to the tested d374 config (checked key by key).
  Folders: `results/` = d374 (was `results_d374/`), `results_d315/` = previous main (with its split-half and FU-only
  sensitivity runs), `results_d437/` = d433. Configs `config/params_d315.yaml`, `config/params_d437.yaml`.
  The split-half stability check was run on d315, not yet on d374.
- **[2026-10-02] Claude Cloud classifier panel merged and run on d374 (07a/07b), plus new step 07g (published classes,
  head-to-head).**
  - **Our NTP templates vs the published calls (FU-iCCA; TCGA / GSE244807 for STIM):** Andersen ARI 0.85; STIM 89% exact
    (ARI 0.76); Lin 2026 81% (0.65); Dong 2022 proteomic 78% (0.52); Oishi ARI 0.47; Sia 2013 poor (67% exact on the 67
    called, ARI 0.10; Cloud also found Sia calls do not transfer to RNA-seq).
  - **Every published class level (61) has ≥ 1 enriched MINER state.** High-risk states S1, S3, S10, S11 carry Andersen
    cluster 2 / Lin SI / large duct; S10–S11 = STIM tumour classical, S1 = inflammatory stroma and Dong S1 (inflammatory);
    low-risk S0 / S4 / S8 = STIM hepatic stem-like, Dong S4 (differentiated), small duct; S7 (lowest risk) = STIM immune
    classical; S13 = desert-like.
  - **Risk score by published class (FU-iCCA, in-sample):** high in Andersen 2, Oishi MH (published label), Dong S1 inflammatory (+1.13) and S2 mesenchymal, Lin SI (+1.34), STIM tumour classical (+1.12) and
    inflammatory stroma; low in Dong S4 differentiated (−0.81), STIM hepatic stem-like (−0.74), Lin SIII. Job 2020 immune
    classes do not separate risk (p 0.12). Sia 2013 is inverted (Inflammation +0.44 > Proliferation −0.46) — consistent with
    the Sia calls not transferring to RNA-seq.
  - **Head-to-head in the held-out cohorts (`results/07_post/published/head_to_head.tsv`):**
    - GSE244807 (230 pts, 137 deaths; Cox stratified by specimen): MINER C 0.67, HR/SD 1.59. STIM classes fitted in the cohort
      C 0.66; Sia 2013 survival signature 0.66; Dong 2022 prognostic biomarkers 0.66. MINER adds to the seven small published
      iCCA signatures and Fan CORE-37 (LR p ≤ 0.002), but **not** to STIM (p 0.11), Sia survival (0.17), Sia recurrence (0.98)
      or Dong biomarkers (0.40), while those add to MINER (p < 0.001).
    - OEP002768 (58 pts, 29 deaths): MINER C 0.69, HR/SD 2.06; Sia recurrence 0.71, Dong biomarkers 0.70, Sia survival 0.69,
      Lin 2026 classes (fitted) 0.67. MINER adds to Lin classes (p 0.006) and to the small signatures; not to Sia / Dong.
    - **Conclusion, as in HCC: the network risk score is as good as the best published iCCA signatures, not better.** Several
      published 4–9-gene signatures do not replicate (C < 0.5 after orienting them in FU-iCCA).

- **[2026-10-02] Discovery designs compared (user: "try 437 and 374 and test").** Configs `config/params_d374.yaml`,
  `config/params_d437.yaml` (results in `results_d374/`, `results_d437/`); comparison `scripts/08d_compare_designs.py` →
  `results/08_validation/design_comparison.tsv`. "437" is 433 in practice: 4 OEP002768 tumours with < 9,000 genes detected
  were dropped. Technical anchor transferred by gene content (`config/technical_anchor_genes.txt`, the 315 run's module 0)
  after the automatic rule picked an immune module in d374 (fixed before the compared runs).
  | | d315 | d374 (+GSE179443) | d433 (+GSE179443 +OEP002768) |
  |---|---|---|---|
  | genes / regulons / regulators / programs | 13,782 / 3,572 / 398 / 164 | 13,504 / 3,451 / 376 / 158 | 11,501 / 2,833 / 314 / 166 |
  | regulators shared with d315 | — | 90% | 76% |
  | high-confidence flows (IDH1 / FGFR2 families) | 6,205 (80 / 68) | 5,832 (50 / 96) | 5,886 (17 / 78) |
  | GSE244807 stratified HR/SD (p) | 1.32 (0.025) | **1.59 (1e-4)** | 1.53 (6e-4) |
  | GSE244807 surgical C / HR/SD | 0.62 / 1.50 | 0.63 / 1.70 | 0.64 / 1.70 |
  | GSE244807 biopsy HR/SD (p) | 1.14 (0.27) | 1.36 (0.012) | 1.29 (0.040) |
  | OEP002768 C / HR/SD | 0.70 / 2.18 (held out) | 0.69 / 2.06 (held out) | 0.65 / 1.90 (in network) |
  | TCGA / GSE107943 C (program ridge) | 0.58 / 0.68 | 0.56 / 0.69 | 0.57 / 0.70 |
  - **Reading:** adding GSE179443 improves external validation in GSE244807 (both strata) at almost no gene cost and keeps
    OEP002768 as an independent test. Adding OEP002768 on top costs 2,000 genes and 24% of the regulators, weakens the IDH1
    and BAP1 causal signal, and does not improve any external test. **Recommendation: d374, OEP002768 held out.**
  - Program-level correspondence between designs is low by gene sets (median best Jaccard 0.06) — consistent with the
    split-half result that regulon membership is not reproducible; compare designs by regulators and activity, not genes.

- **[2026-10-02] Two more cohorts assessed for model building (decision pending with the user).**
  - **OEP002768 (FU-CCA; Deng et al., Hepatology 2023):** user added `Supplementary_Table_1.xlsx`; sheets exported to
    `data/OEP002768/tables/`. 217 CCA patients, 114 iCCA; 84 iCCA tumours with RNA-seq, 102 with WES, OS for 113
    (63 deaths), small / large duct labels, proteome.
    - **Patient overlap with FU-iCCA (same hospital): 32 OEP iCCA patients are also in the Dong cohort**, matched on sex,
      age ± 1 and ≥ 3 of 5 identical pre-operative values (CA19-9, ALT, γ-GT, bilirubin, CEA); about 0.5 matches expected
      by chance. List in `config/oep002768_fu_icca_overlap.tsv`. 21 of them have OEP RNA-seq. They must never be
      counted as independent (not in discovery twice, not as validation).
    - **Unique: 63 iCCA tumours with RNA** (58 also with WES; 62 with OS, 36 deaths; 46 small duct, 7 large duct).
    - Expression is FPKM for 12,724 pre-filtered genes only: 11,518 of the current 13,782 network-universe genes are
      present (84%; 6,751 of 7,926 regulon genes). PC1 of the 63 tumours (15% of variance) tracks genes detected
      (r 0.97; minimum 6,273): mild, a few low-complexity samples.
  - **GSE179443 (Yonsei; PMID 35124821):** 137 liver cancers, **59 iCCA** (51 LC4, 8 LC3 "HCC-like"), 78 HCC. The file
    named raw counts is log2(FPKM + 1) (Cufflinks, GENCODE v27; per GEO processing notes). After rescaling to TPM over
    the network genes quality is uniform (11,626–13,062 genes detected, PC1 unrelated to detection); 13,781 of 13,782
    universe genes present. No survival and no genomics in GEO; the authors' LC subtype labels are there.
  - Claude Cloud's classifier branch (`origin/claude/upbeat-keller-9i651f`: ICC signature sets, published labels,
    07b changes) is fetched and will be merged after the discovery design is settled.

- **[2026-10-02] Split-half stability results (step 08b; half-networks built on ~157 tumours each).**
  | | half A held out | half B held out |
  |---|---|---|
  | regulators recovered | 95% | 96% |
  | regulon membership, median best Jaccard | 0.11 | 0.11 |
  | program activity r in the held-out half (median) | 0.83 | 0.80 |
  | same, top-quartile risk-weight programs | 0.84 | 0.81 |
  | driver → regulator edges recovered (MINER-filtered) | 47% | 37% |
  | same, high-confidence | 24% | 20% |
  | risk, FU-iCCA patients of the unseen half: C-index | 0.71 (120 pts, 55 deaths) | 0.76 (124 pts, 39 deaths) |
  | HR per s.d. | 2.03 | 2.58 |
  - Same pattern as HCC LOCO: **regulators and program-level activity are reproducible; exact regulon gene membership is
    not** (median Jaccard 0.11; < 1% of regulons at ≥ 0.5). Analyses should be read at program / regulator level.
  - **Causal edges are only moderately reproducible** (37–47%), and unevenly by driver: BAP1 47–51%, KRAS 33–46%,
    TP53 27–46%, IDH 23–41%, FGFR2 fusion 67% vs 11% (about 14 fusion-positive tumours per half). Each half has half the
    altered tumours, so this is a lower bound, but individual flows should not be over-read without replication.
  - **Risk generalises within FU-iCCA** when both the network and the model exclude the test half (C 0.71 / 0.76). This is
    same-cohort, same-centre performance; across cohorts it is lower (surgical GSE244807 0.62, TCGA 0.58, GSE107943 0.68).
- **[2026-10-02] ICC classifier gene sets and published labels extracted (Claude Cloud, after the network was opened).**
  `scripts/tools/fetch_signature_sources.py` now fetches from the PMC open-data S3 bucket (open-access supplements),
  Elsevier's CDN (Sia, Dong, Chaisaingmongkol) and authors' repositories; PMC article pages answer scripts with a
  CAPTCHA, so NIH author-manuscript supplements (Martin-Serrano Gut tables) are not reachable. Inventory:
  `docs/signature_sources_inventory.md`. `scripts/tools/extract_icc_signatures.py` writes 56 sets (5,014 rows) to
  `config/subtype_signatures_custom.tsv` and 3,272 per-sample calls to `config/icc_published_labels.tsv`.
  - **Sia 2013** (Suppl Table 2): Proliferation 1,402 / Inflammation 163 genes (= the 1,565 in Lin's copy; the PDF has
    Excel-mangled sep-02 … sep-11, mapped to SEPTn); survival (359 poor / 184 good) and recurrence (124 / 202)
    signatures. **Check in Sia's own cohort (GSE32225, DASL, authors' labels, fetched from GEO in Cloud): NTP 93%
    exact (ARI 0.72; 57 / 57 Inflammation, 81 / 92 Proliferation).** In FU-iCCA RNA-seq the two class scores
    correlate r 0.78 and the calls do not agree with Lin's FU-iCCA Sia calls (ARI 0): the FFPE-array signature
    transfers poorly, or Lin's calls differ in method. Treat Sia calls in RNA-seq with caution.
  - **STIM (Martin-Serrano 2023)**: 500 genes from Lin 2026 Table S2A in five blocks of 100 (immune classical,
    inflammatory stroma, hepatic stem-like, tumour classical, desert-like). Order confirmed: 69–100% of each block's
    FU-iCCA genes peak in that class of Lin's FU-iCCA STIM calls. NTP on the published FU-iCCA mRNA reproduces those
    calls: 87% exact, ARI 0.72.
  - **Beaufrère STIM labels** for GSE244807 (246; hepatic stem-like 90, immune classical 57, inflammatory stroma 54,
    tumour classical 34, desert-like 11 = paper Table S2) and TCGA-CHOL (29), from the authors' repository
    (github.com/trislaz/ICCA_prediction, `csv_labels/`); GEO sample titles CK001… = their patient IDs. Their method:
    gene-wise centring, class = highest mean of the class gene set.
  - **Job 2020**: Table S1 = MCP-counter (8 populations used), Boers HSC quiescent / activated / myofibroblast and
    functional sets; the 14 classification signatures are all there (410 genes = Lin's copy). Classes came from
    clustering the 14 scores with no published centroids, so there is no NTP classifier; use the sets and the
    published FU-iCCA I1–I4 calls (Lin 2026).
  - **Dong 2022**: no subgroup gene list is published. Per-patient proteomic subgroups (Table S5E: S1 41, S2 60,
    S3 46, S4 67 = paper) are in the labels file; mRNA templates (top 100 up per subgroup in the published FU-iCCA
    mRNA) are ours and in-sample for FU-iCCA (NTP 79% exact in FU-iCCA, not an independent check). Lin's "Protein"
    calls equal Dong's subgroups (Inflammatory = S1, Mesenchymal = S2, Metabolic = S3, Differentiated = S4).
  - **Lin 2026 (Cell Rep Med)**: NTP template of five ITH-robust subgroups (SI, SII, SIII-1/2/3; 594 genes): 81% exact
    vs Lin's FU-iCCA calls. Table S4D gives Lin's FU-iCCA calls for nine published classifications (Andersen, Oishi,
    Sia, Dong RNA / protein, Nakamura, Lin J 2022 immune, Job, STIM): all in the labels file, so MINER states and
    programs can be compared with published classes in our discovery cohort directly. Also subgroups for GSE89749
    (81) and OEP002768 (84), and seven published iCCA prognostic signatures (ICC_PROGNOSTIC_*, unsigned).
  - **Added**: Fan 2024 30-gene NTP classifier (C1 mesenchymal / immunosuppressive vs C2 metabolic; C2 genes are
    mitochondrial MT- genes), CORE-37 genes, liver- / pancreas-specific contamination markers; Song 2022 large-duct
    vs small-duct tumour-cell templates (top 100 each; S100P / REG4 / TFF vs SPP1 / CRP / VTN) and GSE89749 S100P /
    SPP1 groups; Chaisaingmongkol 2017 ICC-C1 driver genes (51; no full C1 / C2 classifier is published).
  - **Pipeline**: `subtype_signatures.yaml` classifiers sia2013, stim, dong2022, fan2024, duct, lin2026 (class names
    equal the published label names); 07b adds `config/icc_published_labels.tsv` as `pub_<classifier>` sample labels
    (FU-iCCA by patient ID, TCGA by patient barcode; `post.published_labels` in params), so `ntp_vs_labels.tsv`, state
    enrichment and p4 include them (p4 only pairs each published call with its own classifier). Not run on the server yet.

- **[2026-10-02] ICC classifier panel reviewed; sources registered (`config/signature_sources.yaml`).** (First pass:
  the Cloud network blocked PMC / NCBI / publishers; opened by the user, extraction in the entry above.) New `scripts/tools/fetch_signature_sources.py` resolves
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
