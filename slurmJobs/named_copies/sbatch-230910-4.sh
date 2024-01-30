#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --gres=gpu:A100:1
#SBATCH --time=24:00:00
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=daniel.walther@uzh.ch

# session variables
session=$1  # "yymmdd-id"
echo " ${0}: session: ${session}"
checkdir=$2  # starting with "/home/dwalth/..." without trailing slash
echo " ${0}: checkdir: ${checkdir}"
echo " ${0}: --output file name: ${3}"

# train3dunet commands
module load anaconda3
source activate 3dunet

touch ~/data/outputs/chpt-230910-4/nvidia-smi.log
srun nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/outputs/chpt-230910-4/nvidia-smi.log &

touch $checkdir/train3dunet.output
srun train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-$session.yml 2>&1 | tee -a $checkdir/train3dunet.output
