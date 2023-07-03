# cloud

A repo for more efficient work an a cloud computation infrastructure, circumventing the need for tedious manual transfers (e.g., through globus connect, or using scp, etc.) by using the more efficient git.

This repo revolves around using 3D U-Net, written by Adrian Wolny and X Y, which they provide on the respective [GitHub page](https://github.com/wolny/pytorch-3dunet)

## How to `git clone` this repository (repo)
Because this repo is private, https cloning is not supported via CLI (e.g., linux bash interfaces on remote computing clusters) (this includes providing github username and password). Cloning via ssh keys is required (as other methods, e.g., github's so-called personal access tokens, were tried previously and did not succeed). For github's guide on [Cloning with SSH URLs](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-ssh-urls), click that link.

Here is a link to one's [github account associated ssh keys](https://github.com/settings/keys), where one can see whether there are ssh keys already in one's github account, amongst others.

Although this is redundant regarding above guides, I recommend to [generate a new ssh keypair & adding them to your github account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) for every new remote.

Another redundant but useful information is how to actually clone (this repo) via ssh from the CLI (e.g., via Git Bash), assuming correct set up of ssh key pairs (above guides): `git clone git@github.com:radRoy/cloud.git`.

## Installing pytorch-3dunet into your conda environment

### List of commands without comments

```bash
ssh dwalth@login1.cluster.s3it.uzh.ch
screen -S 3dunet_conda_create
module load anaconda3
conda create -n 3dunet
source activate 3dunet
pip install torch --pre --extra-index-url https://download.pytorch.org/whl/nightly/cu116
#python -c 'import torch;print(torch.backends.cudnn.version())'  # to know the version
#python -c 'import torch;print(torch.__version__)'  # to know the version
git clone https://github.com/wolny/pytorch-3dunet ~/data/
pip install -e ~/data/pytorch-3dunet/
pip install tensorboard
train3dunet  # test whether command is found and gives expected error message ('--config ...' required or so)
    # usage: train3dunet [-h] --config CONFIG
    # train3dunet: error: the following arguments are required: --config
# DW: Success.
```

### List of commands with comments

```bash
ssh <shortname>@login1.cluster.s3it.uzh.ch  # 'login1' requests connection to the cluster's login node 1. enables reconnecting from remote computers with `screen`
screen -S 3dunet_conda_create
    # creating a session on login node 1, so that I can detach from the session, shut down the computer, attach to the session from another computer.
conda create -n <envName>  # 3dunet
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
The last output shows that the pytorch-3dunet was installed successfully.

## Usage of pytorch-3dunet

```bash
train3dunet --config data/pytorch-3dunet/resources/3DUnet_lightsheet_boundary/train_config.yml
# <copy the command here used to train a model (adapted paths)>
```
In these `train_config.yml` files the patch size & stride shape are given in [z, y, x]. This is implied from pytorch-3dunet's github repo README.md, under [Input Data Format](https://github.com/wolny/pytorch-3dunet#input-data-format)

U-Net can only handle absolute paths. Therefore, when specifying paths, e.g., when writing the new .yml file, **substitute `/~/` with `/home/dwalth/`**.  
The path `/~/scratch/datasets/imaging03/scaled0.5/train` is invalid.  
The path `/home/dwalth/scratch/datasets/imaging03/scaled0.5/train` is valid.

The input data should be located on the cluster's scratch partition / drive.

### ... on the ScienceCluster

Here is a page about the [resources of the ScienceCluster](https://docs.s3it.uzh.ch/cluster/resources/). Here is a sub page about the [resources of the A100 cards (& other hardware)](https://docs.s3it.uzh.ch/cluster/resources/#hardware) on the ScienceCluster - one A100 GPU has 80.0 GB VRAM, the V100 GPUs are available in flavours of 16.0 GB and 32.0 GB VRAM.

```bash
ssh dwalth@login1.cluster.s3it.uzh.ch
screen -ls
#screen -r unet-trainer-1  # re attach to a session
#screen -S unet-trainer-<%d>  # initialise a session

#sattach / srun
# typical interactive session with large VRAM requirements
module load a100
    # also possible to specify the gpu this way
srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
srun --pty -n 1 -c 4 --gres=gpu --mem=32G --time=03:00:00 bash -l
squeue -s -u dwalth -i 5
    # displays updated output every -i 5 seconds
squeue -s -u dwalth
    # $JOBID.stepno  # need both ID & stepno to attach to this node from another node
sattach $JOBID.$stepno
    # insert values from squeue output

# be sure to pull the newest config files, yamls, etc.
cd ~/data/cloud/
bash pull-script.sh
cd ~

# run the commands
module load anaconda3
source activate 3dunet
#tensorboard --logdir ~/cloud/logs/tblogs-yymmdd/
    # unclear whether necessary
# starting the GPU memory logging process (scientific-workflows)
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230630-0/nvidia-smi.log &
    #[1] 747532
# typical train3dunet execution command (inside an appropriate gpu compute session)
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
<ctrl + Z>
```

29.06.2023:
- jobid.stepno: 3652230.0
```bash
# 30.06.23, screen session 3dunet-230630-0
squeue -s -u dwalth
         STEPID     NAME PARTITION     USER      TIME NODELIST
      3684833.0     bash  standard   dwalth      0:05 u20-computeibmgpu-vesta19
 3684833.extern   extern  standard   dwalth      0:08 u20-computeibmgpu-vesta19
```

## Things to keep an eye on (e.g., potential or exposed bugs)

1. When putting a computer on standby while a screen session is still attached, that screen session will be frozen when reconnecting from anywhere.

## TBD

230630 (friday): hier stehengeblieben
    to do with multichannel input data:
        train3dunet TypeError: when (skipping...) loading datasets (pytorch-3dunet/pytorch3dunet/datasets/hdf5.py - line 75), Accessing groups is expected to be done with bytes or str, not slices (see line 75 for seeing what is being sliced) - to do with the formatting of the hdf5 files, and how the train_config.yml is written (channel no. = 3 or 1, or whatever)
    solution, attempt 1 TBD:
        conda env, install packages torchvision, torchaudio, which Thomas appeared to find necessary, too. Maybe these add some hdf5 handling capabilities relating to image data in hdf5 format (regarding multiple channels)?
            conda: did not work (channels dont have what i want)
            try pip: successful, many requirements already satisfied (torch is installed already)
    solution, attempt 2 TBD:
        reformat dataset to not have 3 sub internal paths /raw/channel1, /channel2... but instead to have one path /raw, where all the 3 channels are located in (C,Z,Y,X) as an **Image Sequence**. Maybe it wants an RGB image, though... idk