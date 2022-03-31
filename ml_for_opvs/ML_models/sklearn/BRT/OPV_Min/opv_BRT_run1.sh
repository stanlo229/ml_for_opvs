#!/bin/bash
#SBATCH --time=00:30:00
#SBATCH --output=/project/6025683/stanlo/ml_for_opvs/ml_for_opvs/ML_models/sklearn/BRT/slurm.out
#SBATCH --error=/project/6025683/stanlo/ml_for_opvs/ml_for_opvs/ML_models/sklearn/BRT/slurm.err
#SBATCH --account=def-aspuru
#SBATCH --nodes=1
#SBATCH --cpus-per-task=48
#SBATCH --mem=12G
module load python
source /project/6025683/stanlo/opv_project/bin/activate
python opv_BRT.py