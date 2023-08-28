#!/usr/bin/bash
#SBATCH --time=24:00:00 --gres=gpu --mem=16G -n 1 -c 4 --quiet

# Type `sbatch <job.sh>`

cd ~/scratch  # probably not necessary for things to run on the scratch drive, but I did not check.
module load anaconda3
source activate pytorch3dunet
srun --quiet tensorboard --logdir ~/data/wolny/checkpoints/checkpoints_230401/logs/  # trying to mute this output.
train3dunet --config ~/data/wolny/configs/config_230402/dw_train_config_230401.yml

echo "End of File reached. Probably a good sign." > ~/scratch/finish_file
cat ~/scratch/finish_file