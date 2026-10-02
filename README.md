# ICC MINER3

Causal and mechanistic regulatory-network model of intrahepatic cholangiocarcinoma (ICC / iCCA) built with MINER3,
replicating the HCC pipeline (`sturkarslan/hcc-miner3`). Data and results never leave the server (see `.gitignore`).

- `config/cohorts.yaml` — cohort registry; `scripts/tools/fetch_icca_cohorts.py` downloads and inventories them.
- `config/params.yaml` — pipeline parameters (sections are added as each step is adapted to ICC).
- `scripts/01_…` to `09_…` — pipeline steps; SLURM wrappers in `scripts/slurm/` (submit from the project root).
- `PROJECT_LOG.md` — decisions, issues and open questions.

Status: data fetched; steps 01–02 run provisionally on three cohorts; MINER on hold (see `PROJECT_LOG.md`).
