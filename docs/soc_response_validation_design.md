# Do ICC network activity patterns recapitulate response to standard-of-care drugs? Validation design

Status: design (2026-10-05); nothing run. ICC version of the HCC design (`hcc-miner3/docs/soc_response_validation_design.md`).
The trial-emulation workflow (synthetic cohorts, DCNA thresholds) is in `docs/trial_emulation_design.md`.
Numbers marked *(verify)* were not re-checked against the primary paper on 2026-10-05; all others were.

## 1. Standard of care and response rates

Most systemic trials are **biliary tract cancer (BTC)** trials. They mix intrahepatic, extrahepatic and gallbladder
tumours; use the intrahepatic subgroup where reported, and flag otherwise. Targeted trials are biomarker-selected,
and their patients are mostly intrahepatic.

### Resectable disease

Surgery, then adjuvant capecitabine (BILCAP) *(verify)*. Response rates do not apply.

### First line, advanced BTC

| Regimen | Trial | n (arm) | ORR | Notes |
|---|---|---|---|---|
| Durvalumab + gemcitabine + cisplatin | TOPAZ-1 | 341 *(verify)* | 26.7% vs 18.7% (GemCis + placebo) | OS HR 0.80 (0.66–0.97) |
| Pembrolizumab + gemcitabine + cisplatin | KEYNOTE-966 | 533 *(verify)* | 28.7% (24.9–32.8) vs 28.5% (24.8–32.6) | OS benefit without an ORR difference |
| Gemcitabine + cisplatin | ABC-02 | 204 *(verify)* | ~26% *(verify)* | former standard |

### Real-world gemcitabine + cisplatin + durvalumab

| Cohort | ORR | DCR |
|---|---|---|
| UK early-access scheme | 29.1% | 61.2% |
| Worldwide multicentre | 32.7% | — |
| India | 29.7% | — |
| Japan (single centre) | 23% | — |
| iCCA-only cohort (2026) | 27.3% | 65.2% |

### Biomarker-selected (later lines; mostly iCCA)

| Drug | Target | Trial | n | ORR |
|---|---|---|---|---|
| Pemigatinib | FGFR2 fusion / rearrangement | FIGHT-202 cohort A (final) | 108 | 37.0% (27.9–46.9) |
| Futibatinib | FGFR2 fusion / rearrangement | FOENIX-CCA2 | 103 | 42% |
| Ivosidenib | IDH1 mutation | ClarIDHy (vs placebo) | 185 *(verify)* | ~2% *(verify)*; benefit is PFS (median 2.7 months), not response |
| Zanidatamab | HER2 amplification / expression | HERIZON-BTC-01 | 80 *(verify)* | 41.3%; 51.6% if IHC 3+ |
| Dabrafenib + trametinib | BRAF V600E | ROAR (BTC cohort) | 43 *(verify)* | 51% (36–67) |
| Pembrolizumab | MSI-H / dMMR | KEYNOTE-158 | small *(verify)* | — |

### Second line, unselected

FOLFOX: ABC-06 ORR ~5% *(verify)*.

### Locoregional and Chinese practice

- HAIC (FOLFOX-HAIC), often combined with lenvatinib + PD-1. Our only patient-level response cohort, **GSE255058**
  (18 biopsies, 9 responders), is from this setting; step 08c was negative.
- TARE.

## 2. What changes compared with HCC

- **The strongest test is the biomarker contrast.** FGFR inhibitors work (37–42%) only in FGFR2-fusion tumours, and
  our network has a replicated causal flow for the fusion: target programs 49, 51, 52, 54, replicating in direction in
  OEP002768 (97%, step 08e).
  - Prediction: FGFR-inhibitor DCNA (fusion-flow regulons) is high in fusion-positive and low in fusion-negative tumours.
  - The predicted ORR in emulated FIGHT-202 / FOENIX cohorts should exceed that in emulated all-comer cohorts by about
    the published margin.
  - This is a real test of mechanism, unlike prognosis.
- **IDH1 / ivosidenib is a built-in negative for ORR.** The drug is cytostatic, so the network should predict a low
  ORR despite a strong IDH-pathway causal signal. If it predicts a high ORR, the "high DCNA = response" rule fails for
  cytostatic drugs.
- **ICI + chemotherapy adds little response.** TOPAZ-1 gives +8 points; KEYNOTE-966 gives 0. The independent-action
  combination model (`trial_emulation_design.md` §1) should give a small increment, and the network immune programs
  set its size.
- **Immune context is a classification, not a gradient.** The STIM inflamed classes are ~35% (immune classical and
  inflammatory stroma); Job 2020 I2 "immunogenic" is ~11%. Both are on our tumours (`config/icc_published_labels.tsv`,
  NTP calls).
- **HER2.** ORR is higher with IHC 3+ than 2+. Test ERBB2 expression / DCNA as a gradient.
- **Large vs small duct.** KRAS, ERBB2 and inflammatory biology sit in large duct; FGFR2 fusions and IDH1 in small
  duct (Song 2022). Use it to check that the eligible pools sit where expected.

## 3. Pre-specified drug → network mapping (freeze before outcome data)

Program IDs are from `config/program_labels.tsv` (d374 network). DCNA (target regulons) is primary; program scores
are the interpretation layer.

| Drug | Target (ChEMBL, to fetch) | Primary DCNA | Programs expected up in responders |
|---|---|---|---|
| Pemigatinib, futibatinib | FGFR1–3 | FGFR2-fusion causal-flow regulons | 49, 51, 52, 54 (fusion targets; stem-like / progenitor) |
| Ivosidenib | IDH1 | IDH-pathway causal-flow regulons | — (expect low ORR) |
| Zanidatamab, trastuzumab-based | ERBB2 | ERBB2 regulons + ERBB2-amp flows | large-duct programs (71, 15, 18) |
| Dabrafenib + trametinib | BRAF, MAP2K1/2 | MAPK regulons | — (pool probably < 10 V600E) |
| Durvalumab, pembrolizumab | CD274, PDCD1 | regulons containing CD274 / PDCD1 / immune checkpoint genes | 74 inflamed / T cells, 81 NK / T, 82 NFKB1 checkpoint, 28 IFN-α |
| Gemcitabine, cisplatin, oxaliplatin, 5-FU | RRM1 / RRM2 (gemcitabine), TYMS (5-FU); none for platinum | stated proxies: proliferation (115, 107, 111, 119), DNA repair (108) | flagged as proxy |
| Lenvatinib (HAIC combos) | VEGFR1–3, FGFR1–4, PDGFRA, KIT, RET | target regulons | — |

## 4. Validation levels (as in HCC)

1. **Patient level.**
   - GSE255058 (HAIC + lenvatinib + PD-1; 18 tumours): too small for training. It is the only cohort for the
     option-C threshold, and only as a sanity check.
   - Candidate cohorts to look for:
     - RNA from TOPAZ-1 / KEYNOTE-966 translational studies (controlled);
     - the 2026 iCCA GemCis + durvalumab cohort with TME characterization (PubMed 41876834; check whether expression
       is deposited);
     - FIGHT-202 / FOENIX biomarker studies.
2. **Subgroup direction in the 374 discovery tumours** (no treated data needed): FGFR2 fusion vs not (FGFR DCNA);
   IDH1 vs not; ERBB2 amp vs not; STIM inflamed vs not (ICI DCNA); large vs small duct.
3. **Trial emulation** (`trial_emulation_design.md`), arms seeded in `config/trials.yaml`.
   - Leave-one-trial-out pairs:
     - FIGHT-202 ↔ FOENIX-CCA2 (FGFR);
     - TOPAZ-1 ↔ KEYNOTE-966 (ICI + GemCis);
     - TOPAZ-1 GemCis arm ↔ KEYNOTE-966 GemCis arm ↔ ABC-02 (chemotherapy anchor).
   - Single arms that can only be checked with a global or control-anchored threshold: ClarIDHy, HERIZON, ROAR.

**Pool sizes** (eligible tumours, our data):
- FGFR2 fusion: 28 FU-iCCA + 7 OEP002768;
- IDH1: ~30 + OEP;
- ERBB2 amplification: ~11–13;
- BRAF V600E: probably < 10, so ROAR cannot be emulated;
- MSI-H: not called.

## Sources

- TOPAZ-1: [NEJM Evidence](https://evidence.nejm.org/doi/full/10.1056/EVIDoa2200015), [ASCO Daily News](https://dailynews.ascopubs.org/do/topaz-1-durvalumab-plus-gemcitabine-and-cisplatin-could-become-new-first-line-standard)
- KEYNOTE-966: [Lancet](https://www.sciencedirect.com/science/article/abs/pii/S0140673623007274), [Translational Cancer Research comparison](https://tcr.amegroups.org/article/view/82431/html)
- Real world:
  - UK early-access scheme: [PMC12427249](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12427249/)
  - Worldwide multicentre: [Eur J Cancer](https://www.sciencedirect.com/science/article/abs/pii/S0959804924008554)
  - India: [JCO Global Oncology](https://ascopubs.org/doi/10.1200/GO.24.00216)
  - Japan: [PMC11764297](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11764297/)
  - iCCA-only cohort: [PubMed 41876834](https://pubmed.ncbi.nlm.nih.gov/41876834/)
- Targeted:
  - FIGHT-202 final: [PMC11190465](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11190465/)
  - FOENIX-CCA2: [HBSN review](https://hbsn.amegroups.org/article/view/119114/html)
  - HERIZON-BTC-01: [ESMO](https://www.esmo.org/oncology-news/zanidatamab-demonstrates-meaningful-clinical-benefit-with-a-manageable-safety-profile-in-patients-with-treatment-refractory-her2-positive-biliary-tract-cancer)
  - ROAR: [Nat Med](https://www.nature.com/articles/s41591-023-02321-8)
  - Ivosidenib: [review](https://www.tandfonline.com/doi/full/10.2147/CMAR.S326060)
- DCNA: [PMC12081869](https://pmc.ncbi.nlm.nih.gov/articles/PMC12081869/)
