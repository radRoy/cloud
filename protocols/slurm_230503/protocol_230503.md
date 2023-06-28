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
I contacted support at this point.

Is this `Killed` behaviour somehow caused by my data?
=> Trying to run everything identically, except for the input data (now from home via uzh vpn):

New Data directories:
/home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/
/home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/val/
/home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/test/

checkpoint directory
/home/dwalth/data/wolny/checkpoints/checkpoints_230503/

```bash
# ssh into the cluster
srun --pty -n 1 -c 4 --gres=gpu --mem=8G --time=24:00:00 bash -l
	# srun: job 895157 queued and waiting for resources
	# srun: job 895157 has been allocated resources
squeue -u dwalth
	# JOBID    USER    STATE        CPU MIN_ME         TIME END_TIME             NODELIST(REASON)
	# 895157   dwalth  RUNNING        4     8G         2:15 2023-05-04T21:07:40  u20-computeibmgpu-vesta20
nvidia-smi --list-gpus
	# GPU 0: NVIDIA A100-SXM4-80GB (UUID: GPU-727ac791-c19c-f970-ee52-ace0e6d52a1f)
		# Note that now, it is an A-100, not a V-100. Maybe different CUDA versions, drivers, that cause problems with the 3D UNet?
module load anaconda3
source activate envWolny
tensorboard --logdir /~/data/wolny/checkpoints/checkpoints_230503/sampleData/
train3dunet --config /home/dwalth/data/wolny/configs/config_230503/dw_train_config_logat25_valat100_sampleData_230503.yml
	# 2023-05-03 21:21:33,822 [MainThread] INFO Dataset - Creating training and validation set loaders...
	# 2023-05-03 21:21:33,822 [MainThread] WARNING Dataset - Cannot find dataset class in the config. Using default 'StandardHDF5Dataset'.
	# 2023-05-03 21:21:34,468 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_450_ds2x.h5...
	# 2023-05-03 21:21:37,527 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	# 2023-05-03 21:21:52,150 [MainThread] INFO HDF5Dataset - Number of patches: 345
	# 2023-05-03 21:21:52,151 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_451_ds2x.h5...
	# 2023-05-03 21:21:54,710 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
		# DW: It appears that the data is the problem... oh nevermind...
	
	# 2023-05-03 21:21:33,821 [MainThread] INFO UNet3DTrainer - Number of learnable params 4081267
	# 2023-05-03 21:21:33,822 [MainThread] INFO Dataset - Creating training and validation set loaders...
	# 2023-05-03 21:21:33,822 [MainThread] WARNING Dataset - Cannot find dataset class in the config. Using default 'StandardHDF5Dataset'.
	# 2023-05-03 21:21:34,468 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_450_ds2x.h5...
	# 2023-05-03 21:21:37,527 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	# 2023-05-03 21:21:52,150 [MainThread] INFO HDF5Dataset - Number of patches: 345
	# 2023-05-03 21:21:52,151 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_451_ds2x.h5...
	# 2023-05-03 21:21:54,710 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	# 2023-05-03 21:22:08,670 [MainThread] INFO HDF5Dataset - Number of patches: 603
	# 2023-05-03 21:22:08,671 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_445_ds2x.h5...
	# 2023-05-03 21:22:12,186 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	# 2023-05-03 21:22:27,488 [MainThread] INFO HDF5Dataset - Number of patches: 1215
	# 2023-05-03 21:22:27,489 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_416_ds2x.h5...
	# 2023-05-03 21:22:33,390 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	# 2023-05-03 21:22:56,444 [MainThread] INFO HDF5Dataset - Number of patches: 859
	# 2023-05-03 21:22:56,445 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_405_A_ds2x.h5...
	# 2023-05-03 21:22:57,433 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	# 2023-05-03 21:23:00,550 [MainThread] INFO HDF5Dataset - Number of patches: 148
	# 2023-05-03 21:23:00,551 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_449_ds2x.h5...
	# 2023-05-03 21:23:02,051 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	# 2023-05-03 21:23:07,350 [MainThread] INFO HDF5Dataset - Number of patches: 310
	# 2023-05-03 21:23:07,350 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_517_ds2x.h5...
	# 2023-05-03 21:23:11,180 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	# 2023-05-03 21:23:28,965 [MainThread] INFO HDF5Dataset - Number of patches: 1925
	# 2023-05-03 21:23:28,966 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_535_ds2x.h5...
	# 2023-05-03 21:23:33,046 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	# 2023-05-03 21:23:49,746 [MainThread] INFO HDF5Dataset - Number of patches: 1815
	# 2023-05-03 21:23:49,747 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/confocal_boundaries/BoundaryConfocal/train/N_422_ds2x.h5...
	# Killed
		# again the same error... or message, rather.
```

Therefore, the current problem is **not** caused by my data set.