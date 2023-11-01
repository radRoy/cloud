# protocol (commands and otherwise) of today

author: Daniel Walther
creation date: 2023.04.04

copying data from the cmd.exe to the cluster:
	- use the globus.org service in the future
	- use rsync for command line transfer use cases in the future

## the `tensorboard` command requesting user input problem:

just run an interactive slurm session with the compute requirements of my otherwise sbatch job request.
first sort out changed file paths (adapt to today).

```bash
# path to the checkpoint directory
    checkpoint_dir: /home/dwalth/data/wolny/checkpoints/checkpoints_230404/
# path to the training datasets
    file_paths:
      - /home/dwalth/scratch/wolny/data/sample_230331/sample_train_reduced/
# path to the val datasets
    file_paths:
      - /home/dwalth/scratch/wolny/data/sample_230331/sample_val_reduced/
# save above info to the config.yml
# transfer the .yml file to the cluster:
	yml file path:
	  - /home/dwalth/data/wolny/configs/dw_train_config_logat25_230404.yml
```

```bash
srun --pty -n 1 -c 4 --gres=gpu:A100 --mem=16G --time=27:00:00 bash -l

module load anaconda3
source activate envWolny
	# should be the same as pytorch3dunet (just a copy), but the code folder in the pytorch-3dunet repo has the same name

# later, I could definitely refer tensorboard to the .yml file, because the directory is the same.
tensorboard --logdir /home/dwalth/data/wolny/checkpoints/checkpoints_230404/
	# give the user input required
# later, I should check out, whether this command already includes the tensorboard logging functionality (!)
train3dunet --config /home/dwalth/data/wolny/configs/dw_train_config_logat25_230404.yml
```

-----
Actually entered the commands like this to accumulate~ the waiting times up to the user input prompt, and do something else until then.
```bash
srun --pty -n 1 -c 4 --gres=gpu:A100 --mem=16G --time=27:00:00 bash -l; module load anaconda3; source activate envWolny; tensorboard --logdir /home/dwalth/data/wolny/checkpoints/checkpoints_230404/
	# job no. ...
	# messages...
	# <user input prompt>

	# srun: job 680908 queued and waiting for resources
^C
	# srun: Job allocation 680908 has been revoked
	# srun: Force Terminated job 680908
```