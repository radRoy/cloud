# commands protocol: sbatch jobscript preparation
# author: Daniel Walther
# creation date: 2023.03.31

ssh dwalth@cluster.s3it.uzh.ch
srun --pty -n 1 -c 8 --time=01:00:00 --gres=gpu --mem=16G bash -l
#nvidia-smi
	# optional (only sensible in interactive sessions) - check what CUDA version is installed
#nvidia-smi -L
	# optional (only sensible in interactive sessions) - check the name of the currently used GPU

module load anaconda3
source activate pytorch3dunet

# ---

tensorboard --logdir ~/scratch/checkpoints_230331/logs/
train3dunet --config ~/data/pytorch-3dunet/resources/3DUnet_confocal_boundary/dw_train_config_reduced.yml
	# ERROR
	2023-03-31 15:49:51,395 [MainThread] ERROR HDF5Dataset - Skipping train set: ~/scratch/wolny/data/sample_230331/sample_train_reduced/
	Traceback (most recent call last):
	FileNotFoundError: [Errno 2] Unable to open file (unable to open file: name = '~/scratch/wolny/data/sample_230331/sample_train_reduced/', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)
	
	2023-03-31 15:49:51,417 [MainThread] ERROR HDF5Dataset - Skipping val set: ~/scratch/wolny/data/sample_230331/sample_val_reduced
	Traceback (most recent call last):
	FileNotFoundError: [Errno 2] Unable to open file (unable to open file: name = '~/scratch/wolny/data/sample_230331/sample_val_reduced', errno = 2, error message = 'No such file or directory', flags = 0, o_flags = 0)
	
	# above results in the python error:
	File "/home/dwalth/.local/lib/python3.9/site-packages/torch/utils/data/dataset.py", line 225, in __init__
		assert len(self.datasets) > 0, 'datasets should not be an empty iterable'  # type: ignore[arg-type]
	AssertionError: datasets should not be an empty iterable

	# checking whether the paths & files exist: They do
	# currently, dw_train_config_reduced.yml uses ~/... paths.
	# do I need to change them to absolute paths?

train3dunet --config ~/data/pytorch-3dunet/resources/3DUnet_confocal_boundary/dw_train_config_reduced_absolute_paths.yml

# --- it works like this (above)

	...
	2023-03-31 16:08:13,195 [MainThread] INFO UNet3DTrainer - Training iteration [213/150000]. Epoch [0/999]
	2023-03-31 16:08:13,362 [MainThread] INFO UNet3DTrainer - Training iteration [214/150000]. Epoch [0/999]
	2023-03-31 16:08:13,528 [MainThread] INFO UNet3DTrainer - Training iteration [215/150000]. Epoch [0/999]
	2023-03-31 16:08:13,697 [MainThread] INFO UNet3DTrainer - Training iteration [216/150000]. Epoch [0/999]
	2023-03-31 16:08:13,864 [MainThread] INFO UNet3DTrainer - Training iteration [217/150000]. Epoch [0/999]
	2023-03-31 16:08:14,029 [MainThread] INFO UNet3DTrainer - Training iteration [218/150000]. Epoch [0/999]
	2023-03-31 16:08:14,199 [MainThread] INFO UNet3DTrainer - Training iteration [219/150000]. Epoch [0/999]
	2023-03-31 16:08:14,363 [MainThread] INFO UNet3DTrainer - Training iteration [220/150000]. Epoch [0/999]
	2023-03-31 16:08:14,532 [MainThread] INFO UNet3DTrainer - Training iteration [221/150000]. Epoch [0/999]
	2023-03-31 16:08:14,699 [MainThread] INFO UNet3DTrainer - Training iteration [222/150000]. Epoch [0/999]
	2023-03-31 16:08:14,865 [MainThread] INFO UNet3DTrainer - Training iteration [223/150000]. Epoch [0/999]
	2023-03-31 16:08:15,030 [MainThread] INFO UNet3DTrainer - Training iteration [224/150000]. Epoch [0/999]
	2023-03-31 16:08:15,200 [MainThread] INFO UNet3DTrainer - Training iteration [225/150000]. Epoch [0/999]
	2023-03-31 16:08:15,366 [MainThread] INFO UNet3DTrainer - Training iteration [226/150000]. Epoch [0/999]
	2023-03-31 16:08:15,534 [MainThread] INFO UNet3DTrainer - Training iteration [227/150000]. Epoch [0/999]
	2023-03-31 16:08:22,191 [MainThread] INFO UNet3DTrainer - Training iteration [228/150000]. Epoch [0/999]
	...
	# yes, now it works.
	# => the python interpreter does not know paths not starting with '/' (I don't know about the '~' though...)
	...
	2023-03-31 16:10:45,240 [MainThread] INFO UNet3DTrainer - Training iteration [500/150000]. Epoch [0/999]
	2023-03-31 16:10:46,065 [MainThread] INFO EvalMetric - ARand: 0.96124404500997
	2023-03-31 16:10:46,068 [MainThread] INFO UNet3DTrainer - Training stats. Loss: 0.4072515987753868. Evaluation score: 0.96124404500997
	2023-03-31 16:10:46,071 [MainThread] INFO UNet3DTrainer - Logging model parameters and gradients
	2023-03-31 16:10:47,768 [MainThread] INFO UNet3DTrainer - Training iteration [501/150000]. Epoch [0/999]
	...
	# the first validation iteration seems to have worked.