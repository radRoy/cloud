#!/usr/bin/bash
#SBATCH --time=24:00:00  # upper runtime (duration) limit <hh:mm:ss>
#SBATCH --gres=gpu:A100  # gener. cons. resources (gpu:name:ncores)
#SBATCH -c 4  # --cpus-per-task=<ncpus>
#SBATCH --mem=16G  # needed memory depends on the input (to unet) data set
#SBATCH -Q  # --quiet
 # Suppress informational messages from sbatch such as Job ID. Only errors will still be displayed.
 # Use case: E.g., when a command in this file requires some user input to finish,
  # blocking execution of the next line of code in this script
  # (because slurm jobs don't give user input (afaik)).

# could omit these SBATCH flags for the 3d unet
#SBATCH -n 1  # --ntasks=<ntasks>

# Type `sbatch <job.sh>` into the console to use above comments as arguments, instead of ignoring them,
 # and thus submit this bash script as a slurm job,
 # and then still run it just the same as when typing `<job.sh>` into the console.

# SLURM_SUBMIT_DIR = "~/"
# cd $SLURM_SUBMIT_DIR

cd ~/scratch  # probably not necessary for things to run on the scratch drive, but I did not check.
module load anaconda3
source activate pytorch3dunet
tensorboard --logdir ~/scratch/checkpoints_230401/logs/
train3dunet --config ~/data/pytorch-3dunet/resources/3DUnet_confocal_boundary/dw_train_config_reduced_absolute_paths.yml

echo "End of File reached. Probably a good sign." > ~/scratch/finish_file
cat ~/scratch/finish_file