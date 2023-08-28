# commands protocol: pytorch 3d unet `sbatch` slurm job script 
author: Daniel Walther
creation date: 2023.03.31

Opened `cmd.exe` on Windows 10.
```bash
ssh dwalth@cluster.s3it.uzh.ch
cd ~
#srun --pty -n 1 -c 8 --time=01:00:00 --gres=gpu --mem=16G bash -l  # interactive gpu compute session
```

Then I wrote the jobscript (currently) named `pyto3dun-train.sh`, mainly with ESC401 coursework, also with googling:  
```bash
nano data/jobs/pyto3dun-train.sh
```
...which resulted in this:
```bash
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
tensorboard --logdir ~/scratch/checkpoints_230331/logs/
train3dunet --config ~/data/pytorch-3dunet/resources/3DUnet_confocal_boundary/dw_train_config_reduced_absolute_paths.yml

echo "End of File reached. Probably a good sign." > ~/scratch/finish_file
cat ~/scratch/finish_file
```

Then I executed the job script wih the `sbatch` command:
```bash
sbatch data/jobs/pyto3dun-train.sh
	# output
	Submitted batch job 665646

dwalth@u20-login-3:~$ squeue -u dwalth  # minutes later
	# output
	JOBID    USER    STATE        CPU MIN_ME         TIME END_TIME             NODELIST(REASON)
	665646   dwalth  RUNNING        4    16G         6:04 2023-04-01T22:10:04  u20-computeibmgpu-vesta19
```

Now, I wait (Friday, 2023.03.31, 22:34).