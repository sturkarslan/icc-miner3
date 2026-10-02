# ICC MINER3

Causal and mechanistic regulatory-network model of intrahepatic cholangiocarcinoma (ICC / iCCA) built with MINER3,
replicating the HCC pipeline (`sturkarslan/hcc-miner3`). Data and results never leave the server (see `.gitignore`).

- `config/cohorts.yaml` — cohort registry; `scripts/tools/fetch_icca_cohorts.py` downloads and inventories them.
- `config/signature_sources.yaml` — published iCCA classifier papers; `scripts/tools/fetch_signature_sources.py` downloads
  their supplements and writes `docs/signature_sources_inventory.md` for the gene-list extraction scripts.
- `config/params.yaml` — pipeline parameters (sections are added as each step is adapted to ICC).
- `scripts/01_…` to `09_…` — pipeline steps; SLURM wrappers in `scripts/slurm/` (submit from the project root).
- `PROJECT_LOG.md` — decisions, issues and open questions.

Discovery cohort: FU-iCCA (255 tumours). Validation: GSE244807, TCGA-CHOL, GSE107943 and others. See `PROJECT_LOG.md` for status.
