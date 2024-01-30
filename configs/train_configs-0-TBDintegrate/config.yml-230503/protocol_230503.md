# protocol (commands and otherwise) of today

author: Daniel Walther
creation date: 2023.05.03

```bash
# ssh into cluster
srun --pty -n 1 -c 4 --gres=gpu --mem=8G --time=24:00:00 bash -l
squeue -u dwalth
	JOBID    USER    STATE        CPU MIN_ME         TIME END_TIME             NODELIST(REASON)
	891750   dwalth  RUNNING        4     8G         0:08 2023-05-04T16:51:52  u20-computeibmgpu-vesta11
nvidia-smi --list-gpus
	GPU 0: Tesla V100-SXM2-32GB (UUID: GPU-148c21e3-6554-6870-e74a-710d75fa8cf1)
```

In all filepaths: when writing the new .yml file: Substitute `/~/` with `/home/dwalth/` (UNet can only work with absolute paths, at least when training it like this).

Are the .h5 files in the right inline formatting?
	=> Yes (from memory). And also on the cluster's scratch directory.
Data directories:
/~/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/
/~/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/val/
/~/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/test/

checkpoint directory
/~/data/wolny/checkpoints/checkpoints_230503/babb2.1-autofluo-3-1-1/

paremeters:
trainer:
  # model with lower eval score is considered better
  eval_score_higher_is_better: False
  # path to the checkpoint directory
  checkpoint_dir: /home/dwalth/data/wolny/checkpoints/checkpoints_230503/babb2.1-autofluo-3-1-1/
  # path to latest checkpoint; if provided the training will be resumed from that checkpoint
  resume: null
  # path to the best_checkpoint.pytorch; to be used for fine-tuning the model with additional ground truth
  pre_trained: null
  # how many iterations between validations
  validate_after_iters: 100
  # how many iterations between tensorboard logging
  log_after_iters: 25
  # max number of epochs
  max_num_epochs: 5
  # max number of iterations
  max_num_iterations: 5000

```bash
module load anaconda3
source activate envWolny
tensorboard --logdir /~/data/wolny/checkpoints/checkpoints_230503/babb2.1-autofluo-3-1-1/
train3dunet --config /home/dwalth/data/wolny/configs/config_230503/dw_train_config_logat25_valat100_230503.yml
	# ~verbose output:
	2023-05-03 17:36:20,371 [MainThread] WARNING Dataset - Cannot find dataset class in the config. Using default 'StandardHDF5Dataset'.
	2023-05-03 17:36:21,138 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/babb2.1-a5-05-otsuLabelled.h5...
	2023-05-03 17:36:39,753 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	2023-05-03 17:37:40,935 [MainThread] INFO HDF5Dataset - Number of patches: 187
	2023-05-03 17:37:40,936 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/babb2.1-a5-02-otsuLabelled.h5...
	Killed
	
	# ok, looks normal, yeah this warning message usually comes up
	# ...Killed??? ehm... why? WTF

train3dunet --config /home/dwalth/data/wolny/configs/config_230503/dw_train_config_logat25_valat100_230503.yml
	2023-05-03 17:44:59,390 [MainThread] INFO HDF5Dataset - Number of patches: 187
	2023-05-03 17:44:59,391 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/babb2.1-a5-02-otsuLabelled.h5...
	Killed
	# again.. some verbose mode?
	# no, there is only the very limited -h help (which is almost nothing) and the --config flag. no man, too.
```