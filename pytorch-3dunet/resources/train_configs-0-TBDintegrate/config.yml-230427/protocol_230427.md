# protocol (commands and otherwise) of today

author: Daniel Walther
creation date: 2023.04.27

copied ground truth (autofluorescence 488nm Intensity 50 %) and label data with globus (some downloadable executable for transferring files from/to the local device, see for instance <https://user.cscs.ch/storage/transfer/external/> and there <https://www.globus.org/globus-connect-personal>. I originally found the Globus Connect Personal tool inside Globus. very well made interface, rather self-explanatory.)
	- use the globus.org service in the future (done)
		- possible to add the GroupLienkamp network location to my Globus Collections / as a new Globus Collection (= network location)?
	- use rsync for command line transfer use cases in the future (done, refer to s3it uzh website for tutorials & templates)

## the `tensorboard` command requesting user input problem:

just run an interactive slurm session with the compute requirements of my otherwise sbatch job request.
first sort out changed file paths (adapt to today).

In the interactive session submitted & allocated below, the V100 was assigned. Refer to <https://docs.s3it.uzh.ch/cluster/resources/> to see possible resource configurations. I got allocated the 32 GB GPU RAM configuration, today.

```bash
# open cmd.exe
ssh <shortname>@cluster.s3it.uzh.ch
	# arrive in login node
srun --pty -n 1 -c 4 --gres=gpu --mem=32G --time=24:00:00 bash -l
	# (13:51) srun: job 853574 queued and waiting for resources
	# (13:54) srun: job 853574 has been allocated resources
nvidia-smi --list-gpus
	# GPU 0: Tesla V100-SXM2-32GB (UUID: GPU-40988f69-6118-9998-dbcb-ff6bd4e8cebf)

module load anaconda3
source activate envWolny

#tensorboard --logdir /home/dwalth/data/wolny/checkpoints/checkpoints_230427/babb2.1-autofluo-3-1-1/
train3dunet --config /home/dwalth/data/wolny/configs/config_230427/dw_train_config_logat25_230427.yml
	# Does this command include the tensorboard logging functionality?
	# => unknown

	# DW: VERBOSE output documentation below:
	# ...
	# 2023-04-27 14:05:22,714 [MainThread] INFO Dataset - Creating training and validation set loaders...
	# 2023-04-27 14:05:22,714 [MainThread] WARNING Dataset - Cannot find dataset class in the config. Using default 'StandardHDF5Dataset'.
	# 2023-04-27 14:05:23,486 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/babb2.1-a5-05-otsuLabelled.h5...
	# 2023-04-27 14:05:23,538 [MainThread] ERROR HDF5Dataset - Skipping train set: /home/dwalth/scratch/wolny/data/babb2.1/h5-488Int50raw-638Int50label/train/babb2.1-a5-05-otsuLabelled.h5
	# Traceback (most recent call last):
	# 	...
	# 	File "h5py/h5o.pyx", line 190, in h5py.h5o.open
	# KeyError: "Unable to open object (object 'raw' doesn't exist)"
		# DW: the object 'raw' could refer to my hdf5 substack name 'raw' (or 'label' for the label stack) for the raw input image data (the autofluorescence data, in this case)
		# DW: could also refer to something 3d UNet specific... idk
	
	# DW: ...some other error, the last one in this stdoutput:
	# 2023-04-27 14:05:23,727 [MainThread] INFO Dataset - Number of workers for train/val dataloader: 8
	# 2023-04-27 14:05:23,727 [MainThread] INFO Dataset - Batch size for train/val loader: 1
	# Traceback (most recent call last):
	# 	File "/home/dwalth/.local/lib/python3.9/site-packages/torch/utils/data/dataset.py", line 225, in __init__
    # 		assert len(self.datasets) > 0, 'datasets should not be an empty iterable'  # type: ignore[arg-type]
	# AssertionError: datasets should not be an empty iterable

	# Does the error occur when I first enter the tensorboard logdir command? (I predict that yes, it will.)

tensorboard --logdir /home/dwalth/data/wolny/checkpoints/checkpoints_230427/babb2.1-autofluo-3-1-1/
	# DW: ...the usual messages, although a lot quicker now than usually (like 3 seconds and done instead of minute(s))
	# Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
	# TensorBoard 2.11.2 at http://localhost:6006/ (Press CTRL+C to quit)
train3dunet --config /home/dwalth/data/wolny/configs/config_230427/dw_train_config_logat25_230427.yml
	# DW: same errors as above.

# Did something change about the cluster software (e.g., the CUDA version)? The wolny's did certainly not change (I would have had to make/pull those changes manually)
tensorboard --logdir /home/dwalth/data/wolny/checkpoints/checkpoints_230427/confocalReduced-sampledata-test/
train3dunet --config /home/dwalth/data/wolny/configs/config_230427/dw_train_config_logat25_230427-confocalReduced_sampledata.yml
	# ...
	# 2023-04-27 14:38:02,127 [MainThread] WARNING Dataset - Cannot find dataset class in the config. Using default 'StandardHDF5Dataset'.
		# DW: This warning also appears here with wolny's sample data.
	
	# DW: This data works.
	# DW: Conclusion to above errors (with different input data): The input data is the problem. My formatting while saving my data to the .h5 format is not compatible with wolny's formatting.

# Looking at the progress in s3it's TensorBoard Browser App
# It works, the curves are showing learning some learning progress.
```

The errors that occurred in the run with my benchtop data (babb2.1 a5), I think, is most likely due to these following settings in the training .yml (`dw_train_config_logat25_230427`) not being compatible with the way I formatted the .h5 training (& validation) files.
```python
# Configure training and validation loaders
loaders:
  # how many subprocesses to use for data loading
  num_workers: 8
  # path to the raw data within the H5
  raw_internal_path: /raw
  # path to the the label data withtin the H5
  label_internal_path: /label
```

Now, I will let the 3d UNet run on wolny's sample confocal boundary data (the full data set, not reduced as above) for about a day, to first familiarise myself with the TensorBoard stuff and testing a model that ran for a day or so (testing TBD tomorrow):
```bash
# the interactive session from above is still open and stays allocated for about 20 hours or so.
tensorboard --logdir /home/dwalth/data/wolny/checkpoints/checkpoints_230427/confocal-sampledata-test/
train3dunet --config /home/dwalth/data/wolny/configs/config_230427/dw_train_config_logat100_valat500_230427-confocal_sampledata.yml
	# DW: it works, TensorBoard has started to show some graphs from the log files.
```

Prediction of training iterations & epoch iterations until interactive session runs out:
- 1800 train iterations in 28 minutes: 64.3 iterations per minute
- 50k [iter. max. number] / 64 [iter. / min] = 780 min = 13 hours
- 1 epoch in 13 hours, at most
- left over available runtime in current session: 16.00 - 14.00, 22 hours left
- enough for 1.5 epochs ~
What is an 'epoch' in Deep Learning? <https://www.google.com/search?client=firefox-b-d&q=epoch+in+deep+learning>


## 2nd attempt at training 3D-UNet on my own data set (babb2.1)

The .h5 file formatting was indeed different in wolny's sample data:
- wolny's data: just the names `/raw` and `/label`
- my data: something like `babb2.1/a5/01/channel488/Int50/raw`

Assumably, the UNet would have worked if I had changed the lines to the respective sub-h5 path names:
```python
# Configure training and validation loaders
loaders:
  # how many subprocesses to use for data loading
  num_workers: 8
  # path to the raw data within the H5
  raw_internal_path: /babb2.1/a5/01/channel488/Int50/raw
  	# instead of just `/raw`, as it was when I ran it earlier today.
```
But since the names are repeating the overall h5 names and folder names, anyways, I overwrote the same data into the same .h5 files but with simpler internal path names (`/raw` and `/label`, as they are in wolny's by default).

```bash
# open cmd.exe
ssh <shortname>@cluster.s3it.uzh.ch
	# permission denied (publickey, host...)

# alright, then, let's try to reconnect to this session via the web browser...
# apps > active jobs > open in terminal
squeue -s -u dwalth  # show all jobs of user dwalth, also show stepID (required for sattach)
	# STEPID     NAME PARTITION     USER      TIME NODELIST
    # 853574.0     bash  standard   dwalth   5:17:46 u20-computeibmgpu-vesta11
	# 853574.extern   extern  standard   dwalth   5:17:47 u20-computeibmgpu-vesta11
sattach 853574.0  # sattach <jobid.stepid>  (stepid required)
	# DW: works, the UNet training is still running. was not interrupted by my cmd.exe disconnect with the science cluster (happened just before start of this ```bash``` chunk)
	
	# ...
	# 2023-04-27 19:13:41,949 [MainThread] INFO UNet3DTrainer - Training iteration [14845/50000]. Epoch [0/999]
		# DW: The very last iteration
	# slurmstepd: error: *** STEP 853574.0 ON u20-computeibmgpu-vesta11 CANCELLED AT 2023-04-27T19:13:46 ***
	sattach 853574.0
		# sattach: error: Could not get job step info: Job/step already completing or completed
	squeue -s -u dwalth
    	# STEPID     NAME PARTITION     USER      TIME NODELIST
			# DW: seems like there was some connectivity problem. I also had problems with Internet connectivity outside of science cluster things (guess: uzh vpn problem)
```

New try (to run 3dunet on my own babb2.1 a5 data, now with fixed .h5 internal paths) after a break:
```bash
srun --pty -n 1 -c 4 --gres=gpu --mem=8G --time=24:00:00 bash -l
nvidia-smi --list-gpus
	# GPU 0: Tesla V100-SXM2-32GB (UUID: GPU-40988f69-6118-9998-dbcb-ff6bd4e8cebf)

module load anaconda3
source activate envWolny

#tensorboard --logdir /home/dwalth/data/wolny/checkpoints/checkpoints_230427/babb2.1-autofluo-3-1-1/
train3dunet --config /home/dwalth/data/wolny/configs/config_230427/dw_train_config_logat25_230427.yml

