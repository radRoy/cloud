author: Daniel Walther
creation date: 2023.05.10

data dir
	~/scratch/wolny/data/babb02_230509/
	~/scratch/wolny/data/babb02_230509/train/
	~/scratch/wolny/data/babb02_230509/val/
checkpoint dir
	home/dwalth/data/wolny/checkpoints/checkpoints_230510-0/
log dir
	home/dwalth/data/wolny/checkpoints/checkpoints_230510-0/
config file
	~/data/wolny/configs/config_230510-0/
	~/data/wolny/configs/config_230510-0/train_config_230510-0.yml

patch = stride = z*x*y res
[90,217,332]
	Does not work.

Patch > stride works (refer to `protocol_230509.md`).

Done: change the patch size & stride shape in the config file.
```yml
train loader
      # train patch size given to the network (adapt to fit in your GPU mem, generally the bigger patch the better)
      patch_shape: [90, 217, 332]  # = resolution z,x,y = [90,217,332]
      # train stride between patches
      stride_shape: [0, 0, 0]
val loader
      # VAL(DW) patch size given to the network (adapt to fit in your GPU mem, generally the bigger patch the better)
      patch_shape: [90, 217, 332]  # = resolution z,x,y = [90,217,332]
      # VAL(DW) stride between patches
      stride_shape: [0, 0, 0]
```

btw:
```yml
lr_scheduler:
	factor 0.5
	patience 10
```

Previous VRAM usage:
- 4689 MiB / 81920 MiB (on an A100).
hypothesized VRAM usage with only 1 patch (instead of 4), and no stride shape (0,0,0):
- 4689 \* 4 MiB = 18756 MiB
- available resources on a V100 (are there different types on the cluster?):
	- 6 nodes with 8 V100 GPUs with 32.0 GB (not GiB) of VRAM, each(?)
	- 2 nodes with 8 V100 GPUs with 16.0 GB (not GiB) of VRAM, each(?)
- therefore: need to catch a node with 32.0 GB VRAM
- how can I specify this in an `srun` command (how much VRAM)?
- refer to <https://docs.s3it.uzh.ch/cluster/job_submission/#gpus>:  
> *Some nodes have GPUs with a different amount of GPU memory. If your job fails because you run out of GPU memory, you can specifically request the higher-memory nodes by specifying the node type and a memory constraint; i.e., --gres=gpu:V100:1 __--constraint=GPUMEM32GB__. As with the number of GPU devices, you only need to do so when your application runs out of GPU memory on the nodes with 16 GB of on-board memory. Your job will not run faster on a high-memory node. For convience we've added a module for V100's with 32GB GPU RAM, you can simply call module load v100-32g.*
>
> *If you need at least 32GB of GPU RAM and you don't have a preference between the 32GB V100 or 80GB A100 GPUs, you can use the following two flags when submitting your job or interactive session: --gres=gpu:1 --constraint="GPUMEM32GB|GPUMEM80GB". You will then receive whichever GPU is first available (and cost contributions will apply according to the GPU you receive).*

Note the change to `--gres=gpu:V100` instead of `A100`, as for this job, the 20 GB VRAM (actually 16 or 32, refer to above list) on the V100 should suffice (if the VRAM usage scales linearly with patch size difference, and some other assumptions, I suppose...).
```bash
ssh dwalth@login1.cluster.s3it.uzh.ch

screen -S slurm_230510-0
<ctrl + A + D>  # detach from screen
screen -ls
	There is a screen on:
			1342097.slurm_230510-0  (05/10/23 07:57:19)     (Detached)
	1 Socket in /run/screen/S-dwalth.
screen -x slurm_230510-0
	# now inside the screen session

srun --pty -n 1 -c 8 --gres=gpu:V100:1 --constraint=GPUMEM32GB --mem=128G --time=24:00:00 bash -l
	srun: job 1170752 queued and waiting for resources
	srun: job 1170752 has been allocated resources
squeue -s -u dwalth
			STEPID     NAME PARTITION     USER      TIME NODELIST
		1170752.0     bash  standard   dwalth      0:25 u20-computeibmgpu-vesta11
	1170752.extern   extern  standard   dwalth      0:25 u20-computeibmgpu-vesta11
nvidia-smi --list-gpus
	GPU 0: Tesla V100-SXM2-32GB (UUID: GPU-76470d2f-1e85-0035-c9c5-6a97abc7fe85)

module load anaconda3
source activate envWolny
tensorboard --logdir /home/dwalth/data/wolny/checkpoints/checkpoints_230510-0/
nvidia-smi
	Wed May 10 10:39:57 2023
	+-----------------------------------------------------------------------------+
	| NVIDIA-SMI 510.73.08    Driver Version: 510.73.08    CUDA Version: 11.6     |
	|-------------------------------+----------------------+----------------------+
	| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
	| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
	|                               |                      |               MIG M. |
	|===============================+======================+======================|
	|   0  Tesla V100-SXM2...  On   | 00000000:3B:00.0 Off |                    0 |
	| N/A   30C    P0    41W / 300W |      0MiB / 32768MiB |      0%      Default |
	|                               |                      |                  N/A |
	+-------------------------------+----------------------+----------------------+

	+-----------------------------------------------------------------------------+
	| Processes:                                                                  |
	|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
	|        ID   ID                                                   Usage      |
	|=============================================================================|
	|  No running processes found                                                 |
	+-----------------------------------------------------------------------------+
train3dunet --config ~/data/wolny/configs/config_230510-0/train_config_230510-0.yml
	...
	...train03.h5
		File "/scratch/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 122, in _gen_indices
		for j in range(0, i - k + 1, s):
	ValueError: range() arg 3 must not be zero
	...
	...val04.h5
		File "/scratch/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 122, in _gen_indices
		for j in range(0, i - k + 1, s):
	ValueError: range() arg 3 must not be zero
	...
	...val05.h5
		File "/scratch/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 122, in _gen_indices
		for j in range(0, i - k + 1, s):
	ValueError: range() arg 3 must not be zero
	
	2023-05-10 10:40:29,088 [MainThread] INFO Dataset - Number of workers for train/val dataloader: 8
	2023-05-10 10:40:29,088 [MainThread] INFO Dataset - Batch size for train/val loader: 1
	Traceback (most recent call last):
	  File "/home/dwalth/.local/bin/train3dunet", line 33, in <module>
		sys.exit(load_entry_point('pytorch3dunet', 'console_scripts', 'train3dunet')())
	  File "/scratch/dwalth/pytorch-3dunet/pytorch3dunet/train.py", line 27, in main
		trainer = create_trainer(config)
	  File "/scratch/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 41, in create_trainer
		loaders = get_train_loaders(config)
	  File "/scratch/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 220, in get_train_loaders
		'train': DataLoader(ConcatDataset(train_datasets), batch_size=batch_size, shuffle=True,
	  File "/home/dwalth/.local/lib/python3.9/site-packages/torch/utils/data/dataset.py", line 225, in __init__
		assert len(self.datasets) > 0, 'datasets should not be an empty iterable'  # type: ignore[arg-type]
	AssertionError: datasets should not be an empty iterable
```
Change stride shape to [1,1,1], which I think will not work, but let's try. \*done
```bash
# since globus can currently not communicate with the data drives of the science cluster, I transfer the changed config file the old way:
scp train_config_230510-0.yml dwalth@cluster.s3it.uzh.ch:data/wolny/configs/config_230510-0/
train3dunet --config ~/data/wolny/configs/config_230510-0/train_config_230510-0.yml
	...
	# Skipping train sets, too... just like below with val sets.
	
	...
	Skipping val set (during loading):
		...
	File "/scratch/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 121, in _gen_indices assert i >= k, 'Sample size has to be bigger than the patch size'
	AssertionError: Sample size has to be bigger than the patch size
	
	...
	File "/home/dwalth/.local/lib/python3.9/site-packages/torch/utils/data/dataset.py", line 225, in __init__
    assert len(self.datasets) > 0, 'datasets should not be an empty iterable'  # type: ignore[arg-type]
	AssertionError: datasets should not be an empty iterable
```
The problem is definitely the patch size & stride shape. I have to look deeper into that matter, specifically:
- How can I input only 1 patch & no stride (because striding (stitching between patches) makes no sense with only 1 patch)?
=> On another day. Proof of Principle / Concept is achieved, already.
