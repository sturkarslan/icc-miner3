#!/bin/bash
# After MINER (step 04) for a design: module QC -> technical modules -> regulon filter -> programs/states ->
# causal -> risk -> external validation.  bash scripts/slurm/post_miner_chain.sh config/params_d374.yaml d374 [miner_jobid]
set -euo pipefail
PRM=$1; TAG=$2; DEP=${3:+--dependency=afterok:$3}
S=scripts/slurm
a=$(sbatch --parsable -J ${TAG}_04b $DEP $S/04b_module_qc.sbatch --params $PRM)
b=$(sbatch --parsable -J ${TAG}_04bt --dependency=afterok:$a $S/04b_technical_modules.sbatch --params $PRM)
c=$(sbatch --parsable -J ${TAG}_04c --dependency=afterok:$b $S/04c_filter_regulons.sbatch --params $PRM)
d=$(sbatch --parsable -J ${TAG}_04s --dependency=afterok:$c $S/04_run_miner.sbatch --params $PRM --steps subtypes_filtered)
e=$(sbatch --parsable -J ${TAG}_05 --dependency=afterok:$d $S/05_causal_inference.sbatch --params $PRM)
f=$(sbatch --parsable -J ${TAG}_06 --dependency=afterok:$e $S/06_risk.sbatch --params $PRM)
g=$(sbatch --parsable -J ${TAG}_08 --dependency=afterok:$f $S/08_external_validation.sbatch --params $PRM)
echo "$TAG: 04b $a -> tech $b -> filter $c -> subtypes $d -> causal $e -> risk $f -> validation $g"
