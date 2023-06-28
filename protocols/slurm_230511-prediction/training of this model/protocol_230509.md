author: Daniel Walther
creation date: 2023.05.09

data dir
/~/scratch/wolny/data/babb02_230509/
/~/scratch/wolny/data/babb02_230509/train/
/~/scratch/wolny/data/babb02_230509/val/
checkpoint dir
/~/data/wolny/checkpoints/checkpoints_230509/
log dir
/~/data/wolny/checkpoints/checkpoints_230509/
config file
/~/data/wolny/configs/config_230509/
/~/data/wolny/configs/config_230509/train_config_230509_pat10.yml

patch = stride = z*x*y res
90*217*332
[90,217,332]
	Does not work.

Patch > stride works:
```python
train loader
	# train patch size given to the network (adapt to fit in your GPU mem, generally the bigger patch the better)
      patch_shape: [45, 105, 165]  # = resolution z,x,y = [90,217,332]
      # train stride between patches
      stride_shape: [10, 25, 40]
val loader
	patch_shape: [45, 105, 165]  # = resolution z,x,y = [90,217,332]
		# train stride between patches
		stride_shape: [10, 25, 40]
```
btw: lr_scheduler:
	factor 0.5
	patience 10

```bash
ssh dwalth@login1.cluster.s3it.uzh.ch
screen -S slurm_230509
# now inside the screen session
srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
	srun: job 1166064 queued and waiting for resources
	srun: job 1166064 has been allocated resources
module load anaconda3
source activate envWolny
tensorboard --logdir ~/data/wolny/checkpoints/checkpoints_230509/
train3dunet --config /home/dwalth/data/wolny/configs/config_230509/train_config_230509_pat10.yml
	# it works. eval scores are non-zero. train loss is getting smaller steadily (frequently below 0.25 within 15 minutes training with 3-2-0 train-val-test)
<ctrl + a + d>
	[detached from 994478.slurm_230509]
	[detached from 994478.slurm_230509]
screen -ls
	There is a screen on:
			994478.slurm_230509     (05/09/23 16:38:20)     (Detached)
	1 Socket in /run/screen/S-dwalth.
<ctrl + z>  # pauses a process, too and not only puts it to the background.
bg  # makes a job go to the background (as if ended with `&`, but it's still retrievable mid-execution)
```

memory usage peak:
4691MiB / 81920MiB
processes:
...bin/python (the 3d unet)
```bash
nvidia-smi
	Tue May  9 20:16:10 2023
	+-----------------------------------------------------------------------------+
	| NVIDIA-SMI 510.73.08    Driver Version: 510.73.08    CUDA Version: 11.6     |
	|-------------------------------+----------------------+----------------------+
	| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
	| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
	|                               |                      |               MIG M. |
	|===============================+======================+======================|
	|   0  NVIDIA A100-SXM...  On   | 00000000:C8:00.0 Off |                    0 |
	| N/A   25C    P0    68W / 400W |   4691MiB / 81920MiB |      0%      Default |
	|                               |                      |             Disabled |
	+-------------------------------+----------------------+----------------------+

	+-----------------------------------------------------------------------------+
	| Processes:                                                                  |
	|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
	|        ID   ID                                                   Usage      |
	|=============================================================================|
	|    0   N/A  N/A    647037      C   ...y7vcuhn5nw2s3i/bin/python     4689MiB |
+-----------------------------------------------------------------------------+
```