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
Drug response: each drug's targets (Open Targets) and, for targets that are altered drivers in the network (FGFR2 fusion,
IDH1 mutation, ERBB2 amplification), the regulons of their causal flows were mapped to regulons; their mean activity
(drug-constrained network activity, DCNA) was compared with drug sensitivity in biliary-tract cell lines (PRISM) and with
response rates in published biliary-tract trials.
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
mechanistically rather than in predicting it more accurately. Rebuilding everything on half of the tumours recovers
96% of the regulators and the program activities (r ≈ 0.8), and the risk model built that way still separates the
unseen half (C-index 0.69 and 0.75).

The network also links drugs to tumours through their targets and causal flows. Applied to published biliary-tract
trials, a single activity threshold fitted on the other trials reproduces the biomarker logic of the targeted trials:
emulated FGFR-inhibitor arms drawn from FGFR2-fusion tumours are predicted to respond in about 30% of patients (observed
37–42%), the same drug in FGFR-negative tumours in about 6% (observed 0%), ivosidenib in IDH1-mutant tumours in 6%
(observed 2%) and zanidatamab in ERBB2-amplified tumours in 38% (observed 41%). Across all arms predicted and observed
response rates correlate (r = 0.74; random drug assignments rarely do as well), and the error is smaller than predicting
each arm from the other trials' average. The network overestimates the benefit of adding immunotherapy to
gemcitabine–cisplatin. In biliary-tract cell lines, with only six lines, network activity tracks a general sensitivity
axis rather than drug-specific targeting.

### Legend

**Fig. 2 | Program-based risk, its biology, its validation and drug response.**
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
**e**, DCNA and drug sensitivity in biliary-tract cell lines (PRISM Repurposing secondary screen; 711 drugs whose PRISM
targets map to network regulons, 6 lines with RNA-seq: 4 intrahepatic, 1 extrahepatic, 1 gallbladder; 4,079 line–drug
pairs). DCNA = mean trinary MINER activity of the regulons that a target regulates or belongs to, plus, for FGFR2 / IDH1
/ ERBB2 targets, the signed regulons of their causal flows; lines are predicted responders when DCNA > 0. y axis, PRISM
dose-response AUC standardized within drug (lower = more sensitive). Bars, median and interquartile range. Δ,
difference in mean between classes; label permutation within drug (1,000) and random regulon sets of the same size
(200); the effect is no larger than for random regulons.
**f**, Emulation of published biliary-tract trials (9 arms from 6 trials; ORR and arm size from the publications in
`config/trials.yaml`, baseline sex and age from ClinicalTrials.gov; FIGHT-202 cohort C from its posted results). For
each arm, 1,000 synthetic cohorts of the arm's size were drawn from the discovery tumours that pass the arm's genomic
eligibility (FGFR2 fusion, FGFR2-fusion negative, IDH1 mutant, ERBB2 amplified; pool size in the legend), weighted to the
arm's sex and age. A patient responds if the drug's DCNA exceeds a threshold (combinations: either drug; pembrolizumab
scored through CD274 regulons, PDCD1 being absent from the network; cisplatin, without a protein target, not scored).
One threshold shared by all drugs was fitted on the other trials and applied to the held-out trial. Points, mean
predicted ORR (vertical bars, 95% range over the synthetic cohorts) against observed ORR (horizontal bars, exact binomial
95% CI). Text: Pearson r with the 95th percentile and P of a null in which each arm is scored with randomly chosen drugs;
mean absolute error (MAE) compared with predicting each arm by the mean ORR of the other trials. ROAR (BRAF V600E) could
not be emulated (no BRAF-mutant pool).

---

## Panel → source

| Panel | Result files (under `results/`) |
|---|---|
| 1b | `04_miner/combat/{coexpr,mechinf}`, `05_causal/combat/{highConfidenceCausalResults.csv,regulon_families.tsv}` |
| 1c, 2b, 2c | `04_miner/combat/subtypes_filtered/`, `07_post/subtype_mapping/subtypes_filtered/ntp_calls_*.tsv`, `03_genomics_clinical/` |
| 1d | `07_post/subtype_mapping/subtypes_filtered/program_signature_correlation.tsv` |
| 1e | `05_causal/combat/highConfidenceCausalResults.csv` |
| 1f | `08_validation/OEP002768/causal_replication.tsv` (step 08e) |
| 2a, 2d (in network) | `06_risk/combat/predictor_ridge_programs_FU_iCCA_OS_h36m/`, `06_risk/combat/risk_summary.tsv` |
| 2d (held out) | `08_validation/{GSE244807,OEP002768}/scores.tsv`, `08_validation/summary.tsv` |
| 2e | `10_response/dcna/{celllines_tests.tsv,celllines_pairs.tsv}` (step 10c) |
| 2f | `10_response/trials/{emulation_predictions.tsv,emulation_summary.tsv}` (step 10d) |

Moved out of Figure 2 (2026-10-05; supplementary candidates): HR forest plot (`08_validation/summary.tsv`), C-index vs
published classes and signatures (`07_post/published/head_to_head.tsv`, step 07g) and split-half stability
(`08_validation/split/loco_summary.tsv`, step 08b).
