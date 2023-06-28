# protocol (commands and otherwise) of today

author: Daniel Walther
creation date: 2023.05.04

In all filepaths: when writing the new .yml file: Substitute `/home/dwalth/` with `/home/dwalth/` (UNet can only work with absolute paths, at least when training it like this).

Are the .h5 files in the right inline formatting?
	=> Yes (from memory). And also on the cluster's scratch directory.
Data directories:
/home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/
/home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/val/
/home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/test/

checkpoint directory
/home/dwalth/data/wolny/checkpoints/checkpoints_230504/babb2.1-autofluo-3-1-1/more_iter,less_pat/

config file
/home/dwalth/data/wolny/configs/config_230504/dw_train_config_logat25_valat100_230504-more_iter,less_patience.yml

commands:
```bash
# ssh into cluster
srun --pty -n 1 -c 8 --gres=gpu --mem=128G --time=24:00:00 bash -l
squeue -s -u dwalth
         STEPID     NAME PARTITION     USER      TIME NODELIST
       908783.0     bash  standard   dwalth      3:14 u20-computeibmgpu-vesta6
  908783.extern   extern  standard   dwalth      3:14 u20-computeibmgpu-vesta6
       908784.0     bash  standard   dwalth      3:10 u20-computeibmgpu-vesta6
  908784.extern   extern  standard   dwalth      3:10 u20-computeibmgpu-vesta6
	# this session has jobid = 908784
nvidia-smi --list-gpus
	GPU 0: Tesla V100-SXM2-16GB (UUID: GPU-3e262d5d-0626-9183-de73-27b629371d47)
module load anaconda3
source activate envWolny
tensorboard --logdir /~/data/wolny/checkpoints/checkpoints_230504/babb2.1-autofluo-3-1-1/more_iter,less_pat/
train3dunet --config /home/dwalth/data/wolny/configs/config_230504/dw_train_config_logat25_valat100_230504-more_iter,less_patience.yml
```
Now, the tensorboard checkpoint dir needs to be checked via the [s3it apps](https://apps.s3it.uzh.ch/pun/sys/dashboard/batch_connect/sessions):
