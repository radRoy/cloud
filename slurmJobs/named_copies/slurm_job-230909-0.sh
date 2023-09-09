#!/bin/bash

# session variables
session=$1  # "yymmdd-id"
checkdir=$2  # starting with "/home/dwalth/..." without trailing slash

#SBATCH --ntasks=1         # is this a problem ("job step creation disabled")?
#SBATCH --cpus-per-task=1  # is this a problem ("job step creation disabled")?
#SBATCH --mem=16G
#SBATCH --gres=gpu:A100:1
#SBATCH --time=24:00:00
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=daniel.walther@uzh.ch
#SBATCH --output=slurm-$session.out

# train3dunet commands
module load anaconda3
source activate 3dunet
touch $checkdir/nvidia-smi.log
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f $checkdir/nvidia-smi.log &
touch $checkdir/train3dunet.output
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-$session.yml 2>&1 | tee -a $checkdir/train3dunet.output
