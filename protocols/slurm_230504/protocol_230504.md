# protocol (commands and otherwise) of today

author: Daniel Walther
creation date: 2023.05.04

```bash
# ssh into cluster
srun --pty -n 1 -c 4 --gres=gpu --mem=8G --time=24:00:00 bash -l
	srun: job 904121 queued and waiting for resources
	srun: job 904121 has been allocated resources
nvidia-smi --list-gpus
	GPU 0: Tesla V100-SXM2-16GB (UUID: GPU-1208a58e-ad58-45c4-394a-d9f8723071de)
module load anaconda3
source activate envWolny
squeue -s -u dwalth
         STEPID     NAME PARTITION     USER      TIME NODELIST
       904121.0     bash  standard   dwalth     52:19 u20-computeibmgpu-vesta6
  904121.extern   extern  standard   dwalth     52:20 u20-computeibmgpu-vesta6
```

In all filepaths: when writing the new .yml file: Substitute `/home/dwalth/` with `/home/dwalth/` (UNet can only work with absolute paths, at least when training it like this).

Are the .h5 files in the right inline formatting?
	=> Yes (from memory). And also on the cluster's scratch directory.
Data directories:
/home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/
/home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/val/
/home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/test/

checkpoint directory
/home/dwalth/data/wolny/checkpoints/checkpoints_230503/babb2.1-autofluo-3-1-1/

config file
/home/dwalth/data/wolny/configs/config_230503/dw_train_config_logat25_valat100_230503.yml

```bash
# module load anaconda3
# source activate envWolny
tensorboard --logdir /~/data/wolny/checkpoints/checkpoints_230504/babb2.1-autofluo-3-1-1/
train3dunet --config /home/dwalth/data/wolny/configs/config_230503/dw_train_config_logat25_valat100_230503.yml
	2023-05-04 11:37:21,636 [MainThread] WARNING Dataset - Cannot find dataset class in the config. Using default 'StandardHDF5Dataset'.
	2023-05-04 11:37:22,397 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/babb2.1-a5-05-otsuLabelled.h5...
	2023-05-04 11:37:42,271 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 170, 170], 'stride_shape': [20, 40, 40], 'threshold': 0.6, 'slack_acceptance': 0.01}
	2023-05-04 11:38:41,471 [MainThread] INFO HDF5Dataset - Number of patches: 187
	2023-05-04 11:38:41,472 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/babb2.1-a5-02-otsuLabelled.h5...
	Killed
```
Now, it took a little longer, it seems, until the "Killed" message appears, the first training image even loaded, it seems. But it is still interrupted.

Trying the same thing, but now with more system memory, I read online that reaching system resource limits can cause the Killed message.
```bash
# srun --pty -n 1 -c 8 --gres=gpu --mem=8G --time=24:00:00 bash -l  # above used session (yesterday, too)
srun --pty -n 1 -c 8 --gres=gpu --mem=128G --time=24:00:00 bash -l  # newly used session
	# now requesting 128 GB of RAM, not 8GB
	srun: job 906960 queued and waiting for resources
	srun: job 906960 has been allocated resources
module load anaconda3
source activate envWolny
tensorboard --logdir /~/data/wolny/checkpoints/checkpoints_230504/babb2.1-autofluo-3-1-1/
train3dunet --config /home/dwalth/data/wolny/configs/config_230503/dw_train_config_logat25_valat100_230503.yml
	...
	# 2023-05-04 13:25:08,260 [MainThread] INFO UNet3DTrainer - Training iteration [1350/5000]. Epoch [2/4]
	# 2023-05-04 13:25:08,505 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
	# 2023-05-04 13:25:08,505 [MainThread] INFO EvalMetric - ARand: 0.0
	# 2023-05-04 13:25:08,505 [MainThread] INFO UNet3DTrainer - Training stats. Loss: 0.9902624551093939. Evaluation score: 0.0
	# 2023-05-04 13:25:08,505 [MainThread] INFO UNet3DTrainer - Logging model parameters and gradients
	# 2023-05-04 13:25:09,438 [MainThread] INFO UNet3DTrainer - Training iteration [1351/5000]. Epoch [2/4]
	...
		# DW: Yes, now it works!
```

In another terminal (apps.s3it.uzh.ch > active jobs > open in terminal (within browser) to see the GPU info etc.
```bash
squeue -u dwalth -s
         STEPID     NAME PARTITION     USER      TIME NODELIST
       906960.0     bash  standard   dwalth     24:30 u20-computeibmgpu-vesta20
  906960.extern   extern  standard   dwalth     24:31 u20-computeibmgpu-vesta20
sattach 906960.
	# ... continues running (gives same output as in original terminal. Now, I was hoping it wouldn't and just give me the opportunity to monitor the resource usage statistics.)
^C
	# ... Yes! This cancels only the sattach process, not whatever other command is being run from another terminal session.
	# I wanted to do something like `nvidia-smi -l 1`, found here: https://stackoverflow.com/questions/8223811/a-top-like-utility-for-monitoring-cuda-activity-on-a-gpu
```
=> 3D UNet definitely requires more than 8 GB of memory to run. Regardless of the training data.
TBD: How to make an interactive session continue running when closing the terminal session?

The program finished running:
```bash
	# ...
	# 2023-05-04 13:41:14,276 [MainThread] INFO UNet3DTrainer - Validation iteration 10
	# 2023-05-04 13:41:14,375 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
	# 2023-05-04 13:41:14,375 [MainThread] INFO EvalMetric - ARand: 0.0
	# 2023-05-04 13:41:14,380 [MainThread] INFO UNet3DTrainer - Validation iteration 11
	# 2023-05-04 13:41:14,478 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
	# 2023-05-04 13:41:14,478 [MainThread] INFO EvalMetric - ARand: 0.0
	# 2023-05-04 13:41:14,895 [MainThread] INFO UNet3DTrainer - Validation finished. Loss: 1.6923408806324005. Evaluation score: 0.027758950757232947
	# 2023-05-04 13:41:14,896 [MainThread] INFO UNet3DTrainer - Saving checkpoint to '/home/dwalth/data/wolny/checkpoints/checkpoints_230503/babb2.1-autofluo-3-1-1/last_checkpoint.pytorch'
	# 2023-05-04 13:41:14,959 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
	# 2023-05-04 13:41:14,959 [MainThread] INFO EvalMetric - ARand: 0.0
	# 2023-05-04 13:41:14,959 [MainThread] INFO UNet3DTrainer - Training stats. Loss: 0.9796523726722107. Evaluation score: 0.0
	# 2023-05-04 13:41:14,959 [MainThread] INFO UNet3DTrainer - Logging model parameters and gradients
	# 2023-05-04 13:41:15,848 [MainThread] INFO UNet3DTrainer - Training iteration [3201/5000]. Epoch [4/4]
	# 2023-05-04 13:41:15,952 [MainThread] INFO UNet3DTrainer - Training iteration [3202/5000]. Epoch [4/4]
	# 2023-05-04 13:41:16,122 [MainThread] INFO UNet3DTrainer - Training iteration [3203/5000]. Epoch [4/4]
	# 2023-05-04 13:41:16,292 [MainThread] INFO UNet3DTrainer - Training iteration [3204/5000]. Epoch [4/4]
	# 2023-05-04 13:41:16,460 [MainThread] INFO UNet3DTrainer - Training iteration [3205/5000]. Epoch [4/4]
	# 2023-05-04 13:41:17,780 [MainThread] INFO UNet3DTrainer - Training iteration [3206/5000]. Epoch [4/4]
	# 2023-05-04 13:41:17,884 [MainThread] INFO UNet3DTrainer - Training iteration [3207/5000]. Epoch [4/4]
	# 2023-05-04 13:41:18,052 [MainThread] INFO UNet3DTrainer - Training iteration [3208/5000]. Epoch [4/4]
	# 2023-05-04 13:41:18,220 [MainThread] INFO UNet3DTrainer - Training iteration [3209/5000]. Epoch [4/4]
	# 2023-05-04 13:41:18,389 [MainThread] INFO UNet3DTrainer - Training iteration [3210/5000]. Epoch [4/4]
	# 2023-05-04 13:41:18,948 [MainThread] INFO UNet3DTrainer - Reached maximum number of epochs: 5. Finishing training...
(envWolny) dwalth@u20-computeibmgpu-vesta20:~$
	# Job finished successfulyy.
```
The model appears to stagnate at a training loss of around 0.98 (at the start over 1.1).