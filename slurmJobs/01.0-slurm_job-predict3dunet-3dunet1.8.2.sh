#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --gres=gpu:A100:1
#SBATCH --time=00:15:00
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=daniel.walther@uzh.ch

# info: do not use `srun` in sbatch scripts, except job step creation is enabled (I think this would be done by setting --ntasks to more than 1)

cd ~/data/cloud  # this line appears to be required for below nvidia-smi logging (writing to file) to work.
# bash pull-script.sh

# session variables
session=$1  # "yymmdd-id"
echo " ${0}: session: ${session}"
checkdir=$2  # starting with "/home/dwalth/..." without trailing slash
echo " ${0}: checkdir: ${checkdir}"
echo " ${0}: slurm output file name: ${3}"

# 3dunet commands
#module load mamba  # using mamba not conda, 3dunet1.8.2 was built using mamba, maybe it makes a difference, now.
module load mamba/23.3.1-1  # above line causes an error `Lmod has detected the following error: The following module(s) are unknown: "mamba"`, this results in the end in a gcc related error.
source activate 3dunet1.8.2

touch $checkdir/nvidia-smi.log
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f $checkdir/nvidia-smi.log &

# train3dunet commands
# touch $checkdir/train3dunet.output
# train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-$session.yml 2>&1 | tee -a $checkdir/train3dunet.output

# predict3dunet commands
touch $checkdir/predict3dunet.output
predict3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/test_config-$session.yml 2>&1 | tee -a $checkdir/predict3dunet.output
