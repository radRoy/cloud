# protocol (commands and otherwise) of today

author: Daniel Walther
creation date: 2023.05.04

For running multiple shell sessions within one terminal window, including closing terminal windows without stopping slurm jobs within one of the shell sessions, look at [this Tutorial](https://docs.rc.fas.harvard.edu/kb/gnu-screen/) by some department of Harvard school ~.


In all filepaths: when writing the new .yml file: Substitute `/home/dwalth/` with `/home/dwalth/` (UNet can only work with absolute paths, at least when training it like this).

Are the .h5 files in the right inline formatting?
	=> Yes (from memory). And also on the cluster's scratch directory.
Data directories:
/home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/
/home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/val/
/home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/test/

checkpoint directory
/home/dwalth/data/wolny/checkpoints/checkpoints_230504/babb2.1-autofluo-3-1-1/more_iter/

config file
/home/dwalth/data/wolny/configs/config_230504/dw_train_config_logat25_valat100_230504-more_iter.yml

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
	# this session has jobid = 908783
nvidia-smi --list-gpus
	GPU 0: Tesla V100-SXM2-16GB (UUID: GPU-04f056e3-e2fa-8620-9ad2-12eb11f20d3e)
module load anaconda3
source activate envWolny
tensorboard --logdir /~/data/wolny/checkpoints/checkpoints_230504/babb2.1-autofluo-3-1-1/more_iter/
train3dunet --config /home/dwalth/data/wolny/configs/config_230504/dw_train_config_logat25_valat100_230504-more_iter.yml
	... 
	# 2023-05-04 17:30:44,334 [MainThread] INFO UNet3DTrainer - Training iteration [125/100000]. Epoch [0/4999]
	# 2023-05-04 17:30:45,146 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
	# 2023-05-04 17:30:45,146 [MainThread] INFO EvalMetric - ARand: 0.0
	# 2023-05-04 17:30:45,146 [MainThread] INFO UNet3DTrainer - Training stats. Loss: 1.0188090884685517. Evaluation score: 0.0
	# 2023-05-04 17:30:45,146 [MainThread] INFO UNet3DTrainer - Logging model parameters and gradients
	# 2023-05-04 17:30:45,846 [MainThread] INFO UNet3DTrainer - Training iteration [126/100000]. Epoch [0/4999]
	...
		# Yes, it works!
```