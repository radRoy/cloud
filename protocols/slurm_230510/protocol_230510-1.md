author: Daniel Walther
creation date: 2023.05.10

**The things in this file were not executed at all. TBD on another day.**

## CHANGE THE DATA DIR (after redownscaling the cropped data)
data dir
	/~/scratch/wolny/data/babb02_230509/
	/~/scratch/wolny/data/babb02_230509/train/
	/~/scratch/wolny/data/babb02_230509/val/
	checkpoint dir
/home/dwalth/data/wolny/checkpoints/checkpoints_230510-0/
	log dir
/home/dwalth/data/wolny/checkpoints/checkpoints_230510-0/
	config file
/~/data/wolny/configs/config_230510-0/
/~/data/wolny/configs/config_230510-0/train_config_230510-0.yml

patch = stride = z*x*y res
[90,217,332]
	Does not work.

Patch > stride works (refer to `protocol_230509.md`).


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

TBD:
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