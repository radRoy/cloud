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
#pip install tensorflow  # cluster can not find this installation - "running on reduced feature set" after `tensorboard --logdir <logdir>`
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
screen -S 3dunet
#screen -r unet-trainer-1  # re attach to a session
#screen -S unet-trainer-<%d>  # initialise a session

#sattach / srun
# typical interactive session with large VRAM requirements
module load a100
    # also possible to specify the gpu this way
srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
srun --pty -n 1 -c 16 --gres=gpu:T4 --mem=60G --time=24:00:00 bash -l
    # one T4 node has 16 cpus and 60G memory and 1 T4 GPU with 16.0 G VRAM
srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
squeue -s -u dwalth -i 5
    # displays updated output every -i 5 seconds
squeue -s -u dwalth
    # $JOBID.stepno  # need both ID & stepno to attach to this node from another node
sattach $JOBID.$stepno
    # insert values from squeue output
# 230706-0
squeue -s -u dwalth
            STEPID     NAME PARTITION     USER      TIME NODELIST
        3815617.0     bash  standard   dwalth      1:51 u20-computeibmgpu-vesta20
    3815617.extern   extern  standard   dwalth      1:51 u20-computeibmgpu-vesta20
nvidia-smi --list-gpus
    GPU 0: NVIDIA A100-SXM4-80GB (UUID: GPU-df7c4519-a24b-b997-9865-061a549f2b56)

# be sure to pull the newest config files, yamls, etc.
cd ~/data/cloud/
bash pull-script.sh
#cd ~  # can stay in that directory, does not matter for running 3dunet commands

# run the commands
module load anaconda3
source activate 3dunet

module load tensorboard
#tensorboard --logdir ~/cloud/logs/tblogs-yymmdd/
    # unclear whether necessary
tensorboard --logdir ~/data/cloud/chpts/chpt-230707-2/
# starting the GPU memory logging process (scientific-workflows)

nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230707-2/nvidia-smi.log &
    [1] 642730
ps
    PID TTY          TIME CMD
 641211 pts/0    00:00:00 bash
 642730 pts/0    00:00:00 nvidia-smi
 642731 pts/0    00:00:00 ps

tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230707-2/
# typical train3dunet execution command (inside an appropriate gpu compute session), and some alternatives
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
```

**Training 3dunet on single channel data (because multi channel data is too hard to get to work, without help):**  

Running multiple models separate from each other (different nodes) but simultaneously (230709):
```bash
ssh dwalth@login1.cluster.s3it.uzh.ch
cd ~/data/cloud/
bash pull-script.sh  # assume that train configs are written

screen -ls
# branch out into separate screen sessions


# session with accumulated single channel data sets
screen -S 3dunet230709-0-accum
srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
squeue -s -u dwalth
            STEPID     NAME PARTITION     USER      TIME NODELIST
        3999613.0     bash  standard   dwalth      0:09 u20-computegpu-3
    3999613.extern   extern  standard   dwalth      0:09 u20-computegpu-3
cd ~/data/cloud/
bash createDirs.sh
    Created directory chpts/chpt-230709-0
module load anaconda3 tensorboard
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230709-0/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230709-0/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-accumulated.yml
    ...
    2023-07-09 23:27:42,489 [MainThread] INFO UNetTrainer - eval_score_higher_is_better: False
    2023-07-09 23:27:43,239 [MainThread] INFO UNetTrainer - Training iteration [1/150000]. Epoch [0/999]
    Traceback (most recent call last):
    File "/home/dwalth/.local/bin/train3dunet", line 33, in <module>
        sys.exit(load_entry_point('pytorch3dunet', 'console_scripts', 'train3dunet')())
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/train.py", line 29, in main
        trainer.fit()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 147, in fit
        should_terminate = self.train()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 174, in train
        output, loss = self._forward_pass(input, target, weight)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 297, in _forward_pass
        output = self.model(input)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/model.py", line 91, in forward
        x = decoder(encoder_features, x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/buildingblocks.py", line 338, in forward
        x = self.upsampling(encoder_features=encoder_features, x=x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/buildingblocks.py", line 418, in forward
        return self.upsample(x, output_size)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 1104, in forward
        output_padding = self._output_padding(
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 662, in _output_padding
        raise ValueError((
    ValueError: requested an output size of torch.Size([5, 12, 31]), but valid sizes range from [3, 11, 29] to [4, 12, 30] (for an input of torch.Size([2, 6, 15]))

#<ctrl z>  # put train3dunet in background
<ctrl a d>  # detach screen session
screen -ls  # verify the screen session still exists
scancel -u dwalth 3999613.0


# session with only the 405 nm single channel data sets
screen -S 3dunet230709-1-405
srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
squeue -s -u dwalth
    #
cd ~/data/cloud
bash createDirs.sh
    Created directory chpts/chpt-230709-1
module load anaconda3 tensorboard
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230709-1/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230709-1/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm.yml
<ctrl z>  # put train3dunet in background
<ctrl a d>  # detach screen session
screen -ls  # verify the screen session still exists


# session with only the 488 nm single channel data sets
screen -S 3dunet230709-2-488
srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
squeue -s -u dwalth
    #
cd ~/data/cloud
bash createDirs.sh
    Created directory chpts/chpt-230709-2
module load anaconda3 tensorboard
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230709-2/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230709-2/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-488nm.yml
<ctrl z>  # put train3dunet in background
<ctrl a d>  # detach screen session
screen -ls  # verify the screen session still exists


# session with only the 561 nm single channel data sets
screen -S 3dunet230709-3-561
srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
squeue -s -u dwalth
    #
cd ~/data/cloud
bash createDirs.sh
    Created directory chpts/chpt-230709-3
module load anaconda3 tensorboard
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230709-3/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230709-3/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-561nm.yml
<ctrl z>  # put train3dunet in background
<ctrl a d>  # detach screen session
screen -ls  # verify the screen session still exists
```

Trying to format the single channel input data with fiji (just the h5 file creation):  
```bash
screen -S 3dunet230710-0-405fiji
srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
    # waiting time too long
srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=24:00:00 bash -l
squeue -s -u dwalth
            STEPID     NAME PARTITION     USER      TIME NODELIST
        4001367.0     bash  standard   dwalth      0:30 u20-computeibmgpu-vesta6
    4001367.extern   extern  standard   dwalth      0:30 u20-computeibmgpu-vesta6
cd ~/data/cloud
bash pull-script.sh
bash createDirs.sh
    Created directory chpts/chpt-230710-0
module load anaconda3 tensorboard
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230710-0/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230710-0/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
    2023-07-10 10:29:13,146 [MainThread] INFO UNetTrainer - eval_score_higher_is_better: False
    2023-07-10 10:29:14,494 [MainThread] INFO UNetTrainer - Training iteration [1/150000]. Epoch [0/999]
    Traceback (most recent call last):
    File "/home/dwalth/.local/bin/train3dunet", line 33, in <module>
        sys.exit(load_entry_point('pytorch3dunet', 'console_scripts', 'train3dunet')())
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/train.py", line 29, in main
        trainer.fit()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 147, in fit
        should_terminate = self.train()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 174, in train
        output, loss = self._forward_pass(input, target, weight)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 297, in _forward_pass
        output = self.model(input)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/model.py", line 91, in forward
        x = decoder(encoder_features, x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/buildingblocks.py", line 338, in forward
        x = self.upsampling(encoder_features=encoder_features, x=x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/buildingblocks.py", line 418, in forward
        return self.upsample(x, output_size)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 1104, in forward
        output_padding = self._output_padding(
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 662, in _output_padding
        raise ValueError((
    ValueError: requested an output size of torch.Size([5, 12, 31]), but valid sizes range from [3, 11, 29] to [4, 12, 30] (for an input of torch.Size([2, 6, 15]))

# change stride shape to size where there is no overlap between adjacent strides /paddings~.
bash pull-script.sh
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
```

## Things to keep an eye on (e.g., potential or exposed bugs)

1. When putting a computer on standby while a screen session is still attached, that screen session will be frozen when reconnecting from anywhere.

## Debugging

Verbose original approach to debugging input data formatting (can skip, just for documnetation purposes):

230630 (friday): hier stehengeblieben
    to do with multichannel input data:
        train3dunet TypeError: when (skipping...) loading datasets (pytorch-3dunet/pytorch3dunet/datasets/hdf5.py - line 75), Accessing groups is expected to be done with bytes or str, not slices (see line 75 for seeing what is being sliced) - to do with the formatting of the hdf5 files, and how the train_config.yml is written (channel no. = 3 or 1, or whatever)
    solution, attempt 1:
        install torchvision, torchaudio (Thomas installed it, too, originally)
        => FAILED (same errors - hdf5 input format was wrong)
    solution, attempt 2:
        reformat dataset to not have 3 sub internal paths /raw/channel1, /channel2... but instead to have one path /raw, where all the 3 channels are located in (C,Z,Y,X) as an **Image Sequence**. Maybe it wants an RGB image, though... idk
        => FAILED (but better than before - expected 3 input channels but got 1)

230703:
    solution, attempt 3:
        process images into RGB format (8 bit per channel - RGB24 (normal RGB)), reformat hdf5 data set
        => promising: "sample size must be bigger than patch shape"
        reformatting hdf5 from zyxc to czyx: this sounds promising: https://github.com/Jack-Etheredge/Brain-Tumor-Segmentation-3D-UNet-CNN/blob/master/BraTS_3DUNetCNN.py

### Wrangling with the Input Data Format (formatting HDF5 data sets) for data with multiple channels (3 autofluorescence laser lines)

This was most relevant in the weeks around 19.06.2023 and 07.07.2023 (at least).

**something specific (idk, TBD fill in, if relevant. otherwise ignore)**

```bash
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
    ...
    # loading works
    ...
    2023-07-06 22:29:51,748 [MainThread] INFO UNetTrainer - eval_score_higher_is_better: False  # last non error message
    Traceback (most recent call last):
    File "/home/dwalth/.local/bin/train3dunet", line 33, in <module>
        sys.exit(load_entry_point('pytorch3dunet', 'console_scripts', 'train3dunet')())
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/train.py", line 29, in main
        trainer.fit()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 147, in fit
        should_terminate = self.train()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 168, in train
        for t in self.loaders['train']:
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 633, in __next__
        data = self._next_data()
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 1345, in _next_data
        return self._process_data(data)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 1371, in _process_data
        data.reraise()
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/_utils.py", line 644, in reraise
        raise exception
    AssertionError: Caught AssertionError in DataLoader worker process 0.
    Original Traceback (most recent call last):
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/utils/data/_utils/worker.py", line 308, in _worker_loop
        data = fetcher.fetch(index)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/utils/data/_utils/fetch.py", line 51, in fetch
        data = [self.dataset[idx] for idx in possibly_batched_index]
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/utils/data/_utils/fetch.py", line 51, in <listcomp>
        data = [self.dataset[idx] for idx in possibly_batched_index]
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/utils/data/dataset.py", line 243, in __getitem__
        return self.datasets[dataset_idx][sample_idx]
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/hdf5.py", line 97, in __getitem__
        label_patch_transformed = self.label_transform(self.label[label_idx])
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/augment/transforms.py", line 21, in __call__
        m = t(m)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/augment/transforms.py", line 323, in __call__
        assert m.ndim == 3
    AssertionError
# This error arises with my 3channel czyx data sets (raw and label internal h5 paths), regardless of input & output channel number in train_config.yml (3,3; 3,1; 1,1).
```

**some other attempts**

```bash
# previous try
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-compositeData.yml
    .../hdf5.py, line 75
    ...
    File "/apps/opt/spack/linux-ubuntu20.04-x86_64/gcc-9.3.0/anaconda3-2023.03-1-emayrkyj4zgh57gt37ztn55cwzrrhstk/lib/python3.10/site-packages/h5py/_hl/group.py", line 330, in __getitem__
        raise TypeError("Accessing a group is done with bytes or str, "
    TypeError: Accessing a group is done with bytes or str,  not <class 'slice'>

train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-sequenceData.yml
    ...
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 120, in _gen_indices
        assert i >= k, 'Sample size has to be bigger than the patch size'
    AssertionError: Sample size has to be bigger than the patch size
    # Solution: adapt patch & stride shape to the downscaled resolution (downscaled images in fiji still have original xy res displayed, too (also the actual scaled res, of course))
<another try with adapted train_config file>
    ...
    <loading works>
    ...
    2023-07-03 17:43:40,328 [MainThread] INFO UNetTrainer - eval_score_higher_is_better: False
    2023-07-03 17:43:41,264 [MainThread] INFO UNetTrainer - Training iteration [1/150000]. Epoch [0/999]
    Traceback (most recent call last):
    File "/home/dwalth/.local/bin/train3dunet", line 33, in <module>
        sys.exit(load_entry_point('pytorch3dunet', 'console_scripts', 'train3dunet')())
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/train.py", line 29, in main
        trainer.fit()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 147, in fit
        should_terminate = self.train()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 174, in train
        output, loss = self._forward_pass(input, target, weight)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 297, in _forward_pass
        output = self.model(input)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/model.py", line 79, in forward
        x = encoder(x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/buildingblocks.py", line 280, in forward
        x = self.basic_module(x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/buildingblocks.py", line 196, in forward
        residual = self.conv1(x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 613, in forward
        return self._conv_forward(input, self.weight, self.bias)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 608, in _conv_forward
        return F.conv3d(
    RuntimeError: Given groups=1, weight of size [32, 3, 1, 1, 1], expected input[1, 1, 50, 125, 125] to have 3 channels, but got 1 channels instead
<ctrl + Z>
<ctrl + A + D>
```

**trying with new data format: uint16 grey values of the label images (only 1 channel) ... 230707-0** (-1 was an attempt where in_channels was set to 1, which caused another error, because input data has 3 channels):

```bash
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
    ...
    # loading works
    ...
    2023-07-07 13:55:14,206 [MainThread] INFO UNetTrainer - eval_score_higher_is_better: False
    # 1 message further than with previous data set (changed label data to grayscale and uint16; also 3 input and 1 output channels)
    2023-07-07 13:55:14,898 [MainThread] INFO UNetTrainer - Training iteration [1/150000]. Epoch [0/999]
    Traceback (most recent call last):
    File "/home/dwalth/.local/bin/train3dunet", line 33, in <module>
        sys.exit(load_entry_point('pytorch3dunet', 'console_scripts', 'train3dunet')())
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/train.py", line 29, in main
        trainer.fit()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 147, in fit
        should_terminate = self.train()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 174, in train
        output, loss = self._forward_pass(input, target, weight)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 297, in _forward_pass
        output = self.model(input)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/model.py", line 91, in forward
        x = decoder(encoder_features, x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/buildingblocks.py", line 338, in forward
        x = self.upsampling(encoder_features=encoder_features, x=x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/buildingblocks.py", line 418, in forward
        return self.upsample(x, output_size)
    # DW: This is the part of the 3dunet that causes the error
    
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 1104, in forward
        output_padding = self._output_padding(
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 662, in _output_padding
        raise ValueError((
    ValueError: requested an output size of torch.Size([5, 12, 31]), but valid sizes range from [3, 11, 29] to [4, 12, 30] (for an input of torch.Size([2, 6, 15]))
```

**now with 1 input channel and 1 output channel instead of 3 and 1 or 3 and 3 respectively:**

```bash
train3dunet ...
    ... all good
    ...
    2023-07-07 14:09:31,163 [MainThread] INFO UNetTrainer - eval_score_higher_is_better: False
    2023-07-07 14:09:31,912 [MainThread] INFO UNetTrainer - Training iteration [1/150000]. Epoch [0/999]
    Traceback (most recent call last):
    File "/home/dwalth/.local/bin/train3dunet", line 33, in <module>
        sys.exit(load_entry_point('pytorch3dunet', 'console_scripts', 'train3dunet')())
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/train.py", line 29, in main
        trainer.fit()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 147, in fit
        should_terminate = self.train()
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 174, in train
        output, loss = self._forward_pass(input, target, weight)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/trainer.py", line 297, in _forward_pass
        output = self.model(input)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/model.py", line 79, in forward
        x = encoder(x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/buildingblocks.py", line 280, in forward
        x = self.basic_module(x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/unet3d/buildingblocks.py", line 196, in forward
        residual = self.conv1(x)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/module.py", line 1501, in _call_impl
        return forward_call(*args, **kwargs)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 613, in forward
        return self._conv_forward(input, self.weight, self.bias)
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 608, in _conv_forward
        return F.conv3d(
    RuntimeError: Given groups=1, weight of size [32, 1, 1, 1, 1], expected input[1, 3, 40, 100, 250] to have 1 channels, but got 3 channels instead
```

Therefore, specifying 3 input channels for the /raw hdf5 internal path with formatting (C,Z,Y,X) is correct (where C is 3 in this case).