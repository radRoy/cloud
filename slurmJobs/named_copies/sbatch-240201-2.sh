#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --gres=gpu:A100:1
#SBATCH --time=10:00:00
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=daniel.walther@uzh.ch

# info: do not use `srun` in sbatch scripts, except job step creation is enabled (I think this would be done by setting --ntasks to more than 1)

cd ~/data/cloud  # this line appears to be required for below nvidia-smi logging (writing to file) to work.
# bash pull-script.sh

if [ $# -gt 3 ]; then
    echo Error. Input no input session expected. Input session with my train3dunet starter script is not supported.
    exit
fi

# session variables
session=$1  # "yymmdd-id"
echo " ${0}: session: ${session}"
checkdir=$2  # starting with "/home/dwalth/..." without trailing slash
output_dir=$checkdir
echo " ${0}: checkdir (= output_dir): ${checkdir}"
echo " ${0}: slurm output file name: ${3}"

# 3dunet commands
#module load mamba  # using mamba not conda, 3dunet1.8.2 was built using mamba, maybe it makes a difference, now.
module load mamba/23.3.1-1  # above line causes an error `Lmod has detected the following error: The following module(s) are unknown: "mamba"`, this results in the end in a gcc related error.
source activate 3dunet1.8.2

echo "command: nvidia_log=$output_dir/nvidia-smi-$session.log"
nvidia_log=$output_dir/nvidia-smi-$session.log
touch $nvidia_log

echo "command: nvidia-smi -i \$CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f \$nvidia_log &"
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f $nvidia_log &

# train3dunet preparation
echo: "command: train3dunet_output=$output_dir/train3dunet-$session.output"
train3dunet_output=$output_dir/train3dunet-$session.output
touch $train3dunet_output

config=/home/dwalth/data/cloud/configs/named_copies/train_config-$session.yml
cp $config $output_dir/
cp $(dirname $0)/$0 $output_dir/  # works

# train3dunet command
train3dunet --config $config 2>&1 | tee -a $train3dunet_output
