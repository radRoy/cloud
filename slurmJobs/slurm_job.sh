#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cputs-per-task=1
#SBATCH --mem=16G
#SBATCH --gres=gpu:A100:1
#SBATCH --time=24:00:00
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=daniel.walther@uzh.ch

cd ~/data/cloud
bash pull-script.sh

source ./getNextSession.sh
session=$(nextSession)
source ./createChptDirs.sh
checkdir=$(createCheckpoint)

module load anaconda3
source activate 3dunet
srun nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f $checkdir/nvidia-smi.log &
srun train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-$session.yml 2>&1 | tee -a $checkdir/train3dunet.output
