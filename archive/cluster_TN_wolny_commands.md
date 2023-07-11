# Installation of the pytorch-3dunet repository

## Installation (creating the conda environment)

[Installation notes](https://github.com/wolny/pytorch-3dunet)

```bash
ssh <shortname>@login1.cluster.s3it.uzh.ch
screen -S 3dunet_session

module load anaconda3
#module load tensorboard  # not needed in this installation run
#module load singularityce  # not needed in this installation run
conda create -n 3dunet
source active 3dunet

(3dunet) conda install pip
(3dunet) pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116python
(3dunet) python -c 'import torch;print(torch.backends.cudnn.version())'
    #8500
(3dunet) python -c 'import torch;print(torch.__version__)'
    #2.0.1+cu117
#(3dunet) $verify torch  # command  'torch' unknown
    #TBD: what does `$verify` do? what does `$verify torch` do?

#<navigate to the cloned repo of interest (to have environment.yml ready, etc.)>
(3dunet) conda install -f environment.yml
    # conda can not find the specified packages on the specified channels

# moving on to manually installing the environment requirements package by package

# previously required to run train3dunet despite the finished installation
(3dunet) pip install tensorflow
(3dunet) conda install yaml  # as trying `train3dunet` said, it requires the package `yaml`
(3dunet) conda install pyyaml
(3dunet) conda install pytest
#(3dunet) conda install pytorch  # already installed
(3dunet) conda install tensorboard

#(3dunet) conda install tqdm setuptools h5py scipy scikit-image
    # failed
(3dunet) conda install tqdm
(3dunet) conda install setuptools  # already installed
(3dunet) conda install h5py
    # can not be installed. Path already exists, but conda can not recognize & uninstall it. Path may have been created by another package manager. => This would be pip, I assume, as I used pip for some stuff above.

(3dunet) conda install python=3.9
(3dunet) pip install h5py
    # ...
    # Installing collected packages: h5py
    # ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    # tensorflow 2.11.1 requires wrapt>=1.11.0, which is not installed.
    # Successfully installed h5py-3.9.0
(3dunet) conda install h5py  # as cluster recommends to use conda first always, then pip. maybe now conda works with h5py
    # CondaVerificationError: The package for keyutils located at /home/dwalth/data/conda/pkgs/keyutils-1.6.1-h166bdaf_0
    # appears to be corrupted. The path 'share/man/man7/asymmetric-key.7'
    # specified in the package manifest cannot be found.
(3dunet) conda uninstall keyutils
    # PackagesNotFoundError: The following packages are missing from the target environment:
    #   - keyutils
(3dunet) conda install keyutils
    # CondaVerificationError: The package for keyutils located at /home/dwalth/data/conda/pkgs/keyutils-1.6.1-h166bdaf_0
    # appears to be corrupted. The path 'share/man/man7/asymmetric-key.7'
    # specified in the package manifest cannot be found.
# moving on. maybe it works like it is.

(3dunet) conda install scipy
(3dunet) conda install scikit-image
    # same error & cause as above with keyutils
    # CondaVerificationError: The package for keyutils located at /home/dwalth/data/conda/pkgs/keyutils-1.6.1-h166bdaf_0
    # appears to be corrupted. The path 'share/man/man7/asymmetric-key.7'
    # specified in the package manifest cannot be found.
# moving on.

#(3dunet) conda install pyyaml  # should already be installed
#(3dunet) conda install pytest  # should already be installed

(3dunet) train3dunet
    #command not found
(3dunet) pip install -e .
(3dunet) train3dunet
    #MemoryError - so command is found, now. but I assume there is too little memory. see testing below
```

```bash
# failed package installations
(3dunet) conda install keyutils
(3dunet) conda install scikit-image
(3dunet) conda install h5py
    #(3dunet) pip install h5py worked, though.
```

Under wolny's installation tips, it says that checking the compatibility with installed CUDA versions, etc. is recommended. Therefore:  
Starting an interactive session with the hardware that is to be used when training models:  
```bash
srun --pty -n 1 -c 16 --time=01:00:00 --gres=gpu:A100:1 --mem=64G bash -l
```

```bash
conda create -n <envName>  # testUnet
#conda install pip
    # pip is installed already on the cluster
pip install torch --pre --extra-index-url https://download.pytorch.org/whl/nightly/cu116
    # installing PyTorch ('torch')
    # all requirements already satisfied (cluster built-in, in its gcc>anaconda3>lib>python3.10)
#pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116python
    # alternative to above (this worked previously for Thomas and for me). Unclear, what Thomas installed 'torchvision' and 'torchaudio' for.

# Checking the versions with a python program, passed in as a string (-c 'print("Hello World")')
python -c 'import torch;print(torch.backends.cudnn.version())'
    #8500
    # DW: the cudnn version used by the pytorch installation
python -c 'import torch;print(torch.__version__)'
    #2.0.0+cu117
    # DW: the torch version

# verify torch - Verification is done below by testing the 'train3dunet' command. The pytorch and cuda and cudnn, etc. versions on the ScienceCluster are indeed compatible

cd ~/data
git clone https://github.com/wolny/pytorch-3dunet
pip install -e data/pytorch-3dunet/
    # DW: installs a project into the activated environment (conda in this case)

    #Defaulting to user installation because normal site-packages is not writeable
    #Obtaining file:///home/shortname/data/pytorch-3dunet
    #  Preparing metadata (setup.py) ... done
    #Installing collected packages: pytorch3dunet
    #  Running setup.py develop for pytorch3dunet
    #Successfully installed pytorch3dunet-1.6.0
#train3dunet
    #no module named 'tensorboard'
pip install tensorboard
train3dunet
    # usage: train3dunet [-h] --config CONFIG
    # train3dunet: error: the following arguments are required: --config
```

...something like that, and then he (Thomas Naert) started getting error messages about hardware & driver incompatibilities and the like.

## Testing

```bash
# Maybe now it runs (given more memory)
srun --pty --time=01:00:00 --gres=gpu bash -l
    # srun: job 3645988 queued and waiting for resources
```

