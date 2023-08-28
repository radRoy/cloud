# installation of github.com/wolny... on the science cluster

ssh dwalth@cluster.s3it.uzh.ch

srun --pty -n 1 -c 2 --time=01:20:00 --gres=gpu:T4:1 --mem=7G bash -l
  srun: job 623159 queued and waiting for resources

cd scratch
  dwalth@u20-computegpu-1:~/scratch$

module load anaconda3
conda create -n envWolny
source activate envWolny
  # source because of s3it stuff. it's still a conda environment, though.

# install prereqs
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116python
  # copied from thomas. tbh, I don't understand what the torchvision and torchaudio do.
  # s3it: always try conda install first before using pip install inside your conda environment (https://www.anaconda.com/blog/using-pip-in-a-conda-environment)
  
  WARNING: The scripts
    lit, cmake, cpack and ctest, convert-caffe2-to-onnx, convert-onnx-to-caffe2 and torchrun
  are installed in '/home/dwalth/.local/bin', which is not on PATH.

python -c 'import torch;print(torch.backends.cudnn.version())'
	8500
  # prints cudnn version (just installed) used by the torch installation
  # python program, passed in as a string (-c)
python -c 'import torch;print(torch.__version__)'
	2.0.0+cu117
  # prints torch version (just installed)
	# hm, why 117 and not 116 (url above)?

# prep -------------------------------------------------------------------------------------
(((
## Sample configuration file for training a 3D U-Net on a task of predicting the boundaries in 3D stack of the Arabidopsis
## ovules acquired with the confocal microscope. Training done with a combination of Binary Cross-Entropy and DiceLoss.
## download from https://osf.io/w38uf/
# <download data sets, then copy it via CLI (`scp` does the job for now)>
)))

mkdir sample_train
mkdir sample_val
mkdir sample_test
<path of dir to copy> scp -r train dwalth@cluster.s3it.uzh.ch:/home/dwalth/scratch/pytorch-3dunet/sample_train/
<path of dir to copy> scp -r val dwalth@cluster.s3it.uzh.ch:/home/dwalth/scratch/pytorch-3dunet/
<path of dir to copy> scp -r test dwalth@cluster.s3it.uzh.ch:/home/dwalth/scratch/pytorch-3dunet/
# <move files around on cluster, so that the sample data is in folders with my names (sample_<train/val..>)
## CEHCKPOINT_DIR: /home/dwalth/scratch/pytorch-3dunet/checkpoints/ 	
## PATH_TO_TRAIN_DIR: /home/dwalth/scratch/pytorch-3dunet/sample_train/
## PATH_TO_VAL_DIR: /home/dwalth/scratch/pytorch-3dunet/sample_val/

# change train_config file appropriately

# copy my train.yaml to local drive from local (on LIWW001:H:\):
scp dwalth@cluster.s3it.uzh.ch:/home/dwalth/scratch/pytorch-3dunet/resources/3DUnet_confocal_boundary/dw_train_config.yml H:\My Documents\cluster-uzh

# activate the wolny install conda environment used for installation (not sure why that would be necessary...)
dwalth@u20-login-2:~/scratch/pytorch-3dunet/resources/3DUnet_confocal_boundary$ source activate ~/data/conda/envs/envWolny

# deactivate the wolny install conda environment... can try with if running 3dunet fails without it.
(envWolny) dwalth@u20-login-2:~/scratch/pytorch-3dunet/resources/3DUnet_confocal_boundary$ source deactivate

# start interactive session (should have come first, at the latest before starting the file transfers / downloads)
dwalth@u20-login-2:~/scratch/pytorch-3dunet/resources/3DUnet_confocal_boundary$ srun --pty -n 1 -c 2 --time=01:30:00 --gres=gpu:T4:1 --mem=7G bash -l

source activate envWolny
# (envWolny) <cluster...> :~$
pip install tensorflow
	successfully installed... (incl. tensorboard)
mkdir scratch/pytorch-3dunet/checkpoints/logs
tensorboard --logdir scratch/pytorch-3dunet/checkpoints/logs/
	...
	Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
	TensorBoard 2.11.2 at http://localhost:6006/ (Press CTRL+C to quit)


# executing the wolny TRAIN3DUNET
train3dunet --config resources/3DUnet_confocal_boundary/dw_train_config.yml
	# prep: Done:
		# download data first
		# write correct paths to train/val/test data into config file first
	fails without tensorboard installed - see above for tensorboard, etc. setup (involves ScienceApps)

# executing the wolny TEST3DUNET
test3dunet --config resources/3DUnet_confocal_boundary/dw_test_config.yml


### -------------------

srun --pty -n 1 -c 8 --time=00:20:00 --gres=gpu:T4:1 --mem=64G bash -l
srun --pty -n 1 -c 8 --time=10:00:00 --gres=gpu --mem=64G bash -l
