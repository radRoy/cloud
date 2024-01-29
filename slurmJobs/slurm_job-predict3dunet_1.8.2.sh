#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --gres=gpu:A100:1
#SBATCH --time=00:30:00
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=daniel.walther@uzh.ch

# info: do not use `srun` in sbatch scripts, except job step creation is enabled (I think this would be done by setting --ntasks to more than 1)

# set working directory
cd ~/data/cloud  # this line appears to be required for below nvidia-smi logging (writing to file) to work.

# session variables
# $input_session $current_session $checkpoint_dir $output_dir $slurmout
input_session=$1  # "yymmdd-id"
current_session=$2  # "yymmdd-id"
checkpoint_dir=$3  # the dir specified by the bash input argument. starting with "/home/dwalth/..." without trailing slash
output_dir=$4  # the dir where this slurm outputs will be saved to.
slurm_out=$5  # the slurm output file / filepath
echo " ${0}: input session: ${input_session}"
echo " ${0}: current session: ${current_session}"
echo " ${0}: checkpoint directory: ${checkpoint_dir}"
echo " ${0}: output directory: ${output_dir}"
echo " ${0}: slurm output file: ${slurm_out}"

if [ input_session == current_session ]; then
    echo "Error. For `predict3dunet`, the input and output session IDs must be different. Exiting program."
    exit
fi

# processing input arguments
config_yaml=~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/test_config-$current_session.yml

# 3dunet commands
module load mamba/23.3.1-1  # above line causes an error `Lmod has detected the following error: The following module(s) are unknown: "mamba"`, this results in the end in a gcc related error.
source activate 3dunet1.8.2

$nvidia_log="${output_dir}/nvidia-smi-${current_session}.log"
touch $nvidia_log  # create file
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f $nvidia_log &  # write gpu log to file in background

##############################################################
# automated yaml reading/writing/handling would be done here #
##############################################################

# predict3dunet commands
predict3dunet --config $config_yaml
#predict3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/test_config-$session.yml 2>&1 | tee -a $checkdir/predict3dunet.output
