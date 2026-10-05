# ICC figure explanations and legends

Figures: `results/09_figures/figure1.{pdf,png}`, `figure2.{pdf,png}` (183 mm, Nature double column). Source data:
`figure{1,2}_source_data.xlsx`. Built by `scripts/09_publication_figures.py` from saved results; program names from
`config/program_labels.tsv` (curated, with evidence); classes, signatures and biology blocks from
`config/reference_panel.yaml`. Discovery design d374 (PROJECT_LOG, 2026-10-02).

---

## Figure 1

### What the figure shows

We built a regulatory network of intrahepatic cholangiocarcinoma from 374 tumours in four cohorts (Chinese, Korean
and US) and asked what it captures. The network organises about 8,000 genes into 158 transcriptional programs and 21
tumour states. The programs fall into the known axis of iCCA biology: an aggressive, large-duct axis (Andersen class 2,
Lin SI, STIM tumour classical, Dong S1 inflammation; KRAS-mutant tumours) and a differentiated, small-duct axis (STIM
hepatic stem-like, Dong S4 differentiation, Andersen class 1; FGFR2-fusion and IDH-mutant tumours), with a separate
immune and stromal block. Tumour states line up with the published classes, which our classifiers reproduce (STIM 89%
and Lin 2026 81% agreement with the authors' calls). Causal inference links driver alterations to regulators and
programs: FGFR2 fusions, for example, act through ZNF219, NR5A2, ONECUT1 and other regulators to switch on the stem-like
and differentiated programs that are protective in the risk model. In an independent cohort with exome data
(OEP002768), the predicted direction of the driver effects on regulons replicates for 97% of TP53 flows, 96% of BAP1
flows and 97% of FGFR2-fusion flows (about 50% expected by chance).

### Legend

**Fig. 1 | A causal and mechanistic regulatory network of intrahepatic cholangiocarcinoma.**
**a**, Study design. Expression from 374 iCCAs (FU-iCCA, n = 255; GSE179443, n = 59; TCGA-CHOL intrahepatic, n = 30;
GSE107943, n = 30) was harmonized to 13,504 genes and batch-corrected (ComBat). MINER inferred regulons, programs and
states; regulons derived from co-expression modules that tracked a technical signal (long nuclear-retained transcripts
following genes detected per sample) were excluded. Causal inference linked 78 genomic features (FU-iCCA exome, copy
number and fusions; TCGA mutations) to regulators and regulons. A ridge risk model on program activity was trained on
FU-iCCA overall survival (36 months) and applied with fixed weights to held-out cohorts: GSE244807 (n = 246; 109
resected, 137 biopsies), OEP002768 (59 patients not shared with FU-iCCA) and GSE255058 (treatment response, n = 18).
**b**, Network size at each level (log scale).
**c**, Mean regulon dysregulation (over- minus under-expressed membership) of each program (rows) in each state
(columns); states clustered (average linkage, correlation distance), programs grouped into biology blocks. Tracks: mean
risk score per state; fraction of tumours in published classes by nearest-template prediction (STIM, Martin-Serrano
2023; proteomic subgroups, Dong 2022; duct type, Song 2022); driver frequencies (viridis scale).
**d**, Pearson correlation across tumours between program activity and published iCCA signatures, with each tumour's
mean expression regressed out of both (purple negative, green positive). Program names coloured by the sign of their
risk weight (red adverse, blue protective). H, MSigDB hallmark.
**e**, Causal flows from FGFR2 fusion (n = 28 tumours) to regulators and programs: the regulators with the largest
effects, one per regulon family. Edges: red, up in fusion-positive tumours; blue, down; dashed, the regulator represses
its regulon; width proportional to |Cohen's d|. Flows are high confidence: Benjamini–Hochberg q ≤ 0.1 for the regulon
and driver–regulator tests, |d| ≥ 0.5, ≥ 25 altered tumours, and the same direction in every cohort tested.
**f**, Replication in OEP002768 (exome driver calls, never used for the network). For each driver with ≥ 5 altered
tumours, the share of its high-confidence driver → regulon effects (one regulon per family) whose direction in
OEP002768 matches the discovery Cohen's d (blue), of which nominally significant (P < 0.05, black), and the mean share
for random regulons with the same predicted directions (red tick; 1,000 draws). TP53 10 altered / 44 wild type; BAP1
8 / 46; FGFR2 fusion 7 / 52; IDH1/2 11 / 43; all empirical P = 0.001 except IDH1 alone (P = 0.09).

---

## Figure 2

### What the figure shows

A risk score built from the network's programs separates patients by overall survival in every test setting. Its
largest weights fall on poor-survival, hypoxia, large-duct and inflammatory-ductal programs (adverse) and on
differentiated, hepatic stem-like and NK / T-cell programs (protective). The score follows the published classes: it
is highest in STIM tumour classical, Dong S1 and Andersen class 2 tumours and lowest in hepatic stem-like, Dong S4 and
class 1 tumours, and network states ordered by the score show a matching gradient of observed survival. In held-out
cohorts the score validates in resected tumours (GSE244807, HR 1.70 per s.d.; OEP002768, HR 2.06) and, more weakly, in
biopsies of advanced disease (HR 1.36). It performs as well as the best published iCCA classifiers and signatures
(STIM classes, Sia 2013 survival and recurrence signatures, Dong 2022 prognostic markers) but does not add to them;
several small published signatures do not replicate. As in our HCC network, its value lies in explaining risk
mechanistically rather than in predicting it more accurately.

### Legend

**Fig. 2 | Program-based risk, its biology and its validation.**
**a**, Largest adverse (red) and protective (blue) weights of the ridge model trained on FU-iCCA overall survival.
**b**, Risk score (within-cohort z) by published class (nearest-template calls, all 374 tumours). Bars, median and
interquartile range; Kruskal–Wallis P.
**c**, States ordered by mean risk score. Top, class and driver fractions; middle, risk score; bottom, observed
survival as GuanRank computed within each cohort with survival (FU-iCCA, TCGA-CHOL, GSE107943; 1, earliest death).
Boxes, median and interquartile range; whiskers, 1.5× interquartile range. State mean risk vs median GuanRank:
Spearman ρ = 0.73, P = 2.8 × 10⁻⁴ (20 states with ≥ 5 tumours).
**d**, Kaplan–Meier curves for the within-cohort top 20% of risk scores versus the rest. TCGA-CHOL and GSE107943 were
in the network but not in the risk model; GSE244807 (resected, biopsies) and OEP002768 were never used. C, Harrell's
C-index; HR, Cox hazard ratio of top 20% vs rest.
**e**, Cox hazard ratio per s.d. of risk score (95% CI) in every test cohort, with a random-effects (DerSimonian–Laird)
pooled estimate over the held-out cohorts (GSE244807 resected and biopsy strata, OEP002768).
**f**, C-index in the held-out cohorts of the network score and of published iCCA classifiers and signatures. Classes
(STIM in GSE244807, the authors' calls; Lin 2026 in OEP002768) are Cox models fitted in the test cohort (optimistic for
them); signatures are scored as mean z (up minus down genes) and, when unsigned, oriented in FU-iCCA. GSE244807 models
are stratified by specimen type. Adding the network score to STIM, Sia 2013 survival or Dong 2022 markers:
likelihood-ratio P ≥ 0.09.
**g**, Split-half stability: the network, causal inference and risk model were rebuilt on a random half of the 374
tumours (stratified by cohort) and compared with the full network. *(Pending: split-half run on d374 in progress.)*

---

## Panel → source

| Panel | Result files (under `results/`) |
|---|---|
| 1b | `04_miner/combat/{coexpr,mechinf}`, `05_causal/combat/{highConfidenceCausalResults.csv,regulon_families.tsv}` |
| 1c, 2b, 2c | `04_miner/combat/subtypes_filtered/`, `07_post/subtype_mapping/subtypes_filtered/ntp_calls_*.tsv`, `03_genomics_clinical/` |
| 1d | `07_post/subtype_mapping/subtypes_filtered/program_signature_correlation.tsv` |
| 1e | `05_causal/combat/highConfidenceCausalResults.csv` |
| 1f | `08_validation/OEP002768/causal_replication.tsv` (step 08e) |
| 2a, 2d (in network), 2e | `06_risk/combat/predictor_ridge_programs_FU_iCCA_OS_h36m/`, `06_risk/combat/risk_summary.tsv` |
| 2d (held out), 2e | `08_validation/{GSE244807,OEP002768}/scores.tsv`, `08_validation/summary.tsv` |
| 2f | `07_post/published/head_to_head.tsv` (step 07g) |
| 2g | `08_validation/split/loco_summary.tsv` (step 08b) |
