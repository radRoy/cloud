#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --gres=gpu:A100:1
#SBATCH --time=00:30:00
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=daniel.walther@uzh.ch

# info: do not use `srun` in sbatch scripts, except job step creation is enabled (I think this would be done by setting --ntasks to more than 1)

cd ~/data/cloud  # this line appears to be required for below nvidia-smi logging (writing to file) to work.
# bash pull-script.sh

if [ $# -lt 4 ]; then
    echo "Error. Input session expected. Input session (folder containing the pytorch checkpoint) is required with my starter script."
    exit
fi

# session variables
input_session=$1
echo " ${0}: input_session: ${input_session}"
session=$2  # "yymmdd-id"
echo " ${0}: session: ${session}"
checkdir=$3  # starting with "/home/dwalth/..." without trailing slash
echo " ${0}: checkdir: ${checkdir}"
output_dir=$checkdir/$session
mkdir $output_dir  # throws an error if it already exists
echo " ${0}: output_dir: ${output_dir}"
echo " ${0}: slurm output file name: ${4}"

# 3dunet commands
#module load mamba  # using mamba not conda, 3dunet1.8.2 was built using mamba, maybe it makes a difference, now.
module load mamba/23.3.1-1  # above line causes an error `Lmod has detected the following error: The following module(s) are unknown: "mamba"`, this results in the end in a gcc related error.
source activate 3dunet1.8.2

nvidia_log=$output_dir/nvidia-smi-$session.log
touch $nvidia_log
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f $nvidia_log &

# predict3dunet preparation
predict3dunet_output=$output_dir/predict3dunet-$session.output
touch $predict3dunet_output
config=/home/dwalth/data/cloud/configs/named_copies/test_config-$session.yml
cp $config $output_dir/
cp ~/$(dirname $0)/$0 $output_dir/  # works

# predict3dunet command
predict3dunet --config $config 2>&1 | tee -a $predict3dunet_output
