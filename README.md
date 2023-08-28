# <u>cloud</u>

A git repo for cloud computation operations/processes. This repo is cloned on the Science Cluster (cluster) and can be used for (automated) transfer of input configurations, output/log files, etc. Ultimately, this repo aims at using [3D U-Net (3dunet)](https://github.com/wolny/pytorch-3dunet).

Info List:
- Notation 'TEMP': In this file, at least, subtitles, etc., containing 'TEMP' are not relevant for long-term usage / documentation. E.g., temporary debugging notes.

## <u>How to `git clone` this repository (repo)</u>
Because this repo is private, https cloning is not supported via CLI (e.g., linux bash interfaces on remote computing clusters) (this includes providing github username and password). Cloning via ssh keys is required (as other methods, e.g., github's so-called personal access tokens, were tried previously and did not succeed). For github's guide on [Cloning with SSH URLs](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-ssh-urls), click that link.

Here is a link to one's [github account associated ssh keys](https://github.com/settings/keys), where one can see whether there are ssh keys already in one's github account, amongst others.

Although this is redundant regarding above guides, I recommend to [generate a new ssh keypair & adding them to your github account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) for every new remote.

Another redundant but useful information is how to actually clone (this repo) via ssh from the CLI (e.g., via Git Bash), assuming correct set up of ssh key pairs (above guides): `git clone git@github.com:radRoy/cloud.git`.

## <u>Overview over my data sets used for training 3dunet</u>

The image processing done on multichannel data sets since the meeting on 2023.06.08 (June) has resulted in an h5 data set of the format (TBD reconstruct by opening h5 image in Fiji).

For further information on the datasets' creation, etc., refer to a separate dedicated git repository [imageProcessTif](https://github.com/radRoy/imageProcessTif/).

## <u>Installing pytorch-3dunet into your conda environment</u>

### <u>List of installation commands without comments</u>

```bash
ssh <shortname>@login1.cluster.s3it.uzh.ch
module load anaconda3
conda create -n 3dunet
source activate 3dunet
pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
    # (*1) alternative command
    # (*2) below comment section for testing output
git clone https://github.com/wolny/pytorch-3dunet ~/data/pytorch-3dunet
pip install -e ~/data/pytorch-3dunet/
pip install tensorboard
train3dunet  # test whether command is found and gives expected error message ('--config ...' required or so)
    # usage: train3dunet [-h] --config CONFIG
    # train3dunet: error: the following arguments are required: --config
# DW: Success.
```

**<u>TEMP Fix ideas surrounding 230821,-28, cluster CUDA version problem</u>**
```bash
# IDEA 1
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116python
    # (*1) alternative command to the above one, in case something should not behave as expected down the line.

# IDEA 2
# refer to the email exchange with the cluster staff (~28.8.2023)
```

### <u>List of installation commands with comments</u>

```bash
ssh <shortname>@login1.cluster.s3it.uzh.ch
    # 'login1' prefix not required, here, but good practice for my project, given the long cluster interactive gpu sessions involved in training 3dunet models. It is also practical to have one long continuous bash history from one cluster login node in case entered commands need to be double-checked.
conda create -n <envName>
    # envName is '3dunet' in my case
#conda install pip
    # pip is installed already on the cluster
# https://pytorch.org/get-started/previous-versions/#v1121 , install either conda or pip command version below
pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
#pip install torch --pre --extra-index-url https://download.pytorch.org/whl/nightly/cu116
    # installing PyTorch ('torch')
    # all requirements already satisfied (cluster built-in, in its gcc>anaconda3>lib>python3.10)
    # DW: included with above pip install command (maybe different versions get installed when not specifying the desired version)
# testing the installation (in a GPU interactive session), and how it should look.
# (*3) alternative, equivalent commands below (+ previous output records)
python
import torch
torch.__version__
    # '1.12.1+cu116'
print(torch.cuda.device_count())
    # 1
print(torch.cuda.current_device())
    # 0
print(torch.cuda.is_available())
    # True
#pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116python
    # alternative to above (this worked previously for Thomas and for me). Unclear, what Thomas installed 'torchvision' and 'torchaudio' for.
    # (*1) reference to above fix IDEA (this is an alternative command that I could try for fixing a problem)

# (*3) alternative commands to above. Equivalent installation checking, more compact commands + console output records of the first or second cluster installation (which worked)
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
    # DW: installs a project into the activated environment (conda in this case). Here, adds the pytorch_egg~ commands 'train3dunet' and 'predict3dunet' to the conda environment, these commands link to the now installed (unpacked~) repo (folder) containing installable files (the cloned pytorch-3dunet repo).

    #Defaulting to user installation because normal site-packages is not writeable
    #Obtaining file:///home/shortname/data/pytorch-3dunet
    #  Preparing metadata (setup.py) ... done
    #Installing collected packages: pytorch3dunet
    #  Running setup.py develop for pytorch3dunet
    #Successfully installed pytorch3dunet-1.6.0
#train3dunet
    #no module named 'tensorboard'
pip install tensorboard
#pip install tensorflow  # cluster can not find this installation - "running on reduced feature set" after `tensorboard --logdir <logdir>`
    # was not required in the past, makes no difference to me
train3dunet
    #usage: train3dunet [-h] --config CONFIG
    #train3dunet: error: the following arguments are required: --config
```
The last output shows that the pytorch-3dunet was installed successfully.

## <u>Usage of pytorch-3dunet</u>

### <u>Instructions on the `train_config.yml` files</u>

U-Net can only handle absolute paths. Therefore, when specifying paths, e.g., when writing the new .yml file, **substitute `/~/` with `/home/dwalth/`**.  
The path `/~/scratch/datasets/imaging03/scaled0.5/train` is invalid.  
The path `/home/dwalth/scratch/datasets/imaging03/scaled0.5/train` is valid.

```bash
train3dunet --config data/pytorch-3dunet/resources/3DUnet_lightsheet_boundary/train_config.yml
# <copy the command here used to train a model (adapted paths)>
```
In these `train_config.yml` files the patch size & stride shape are given in [z, y, x]. This is implied from pytorch-3dunet's github repo README.md, under [Input Data Format](https://github.com/wolny/pytorch-3dunet#input-data-format).

The `patch_shape` and `stride_shape` parameters in the `train_config.yml` (below is the relevant structure of such a .yml file) have to follow certain rules (which are hard to find in the mentioned github repo):  
```yml
loaders:
  num_workers: ...
  raw_internal_path: ...
  label_internal_path: ...
  train: ...
    file_paths: ...
    slice_builder: ...
      name: ...
      patch_shape: [z1, y1, x1]
      stride_shape: [z2, y2, x2]
```  

These rules are:  
- `patch_shape` must be bigger than `stride_shape`

*These rules might include **(TBD: unfinished docmentation of the reconstructed ruleset)***:  
- z, y, x of `patch_shape` have to be >64 each (verify) (written somewhere on wolny's github or in his comments)
- y and x of `patch_shape` have to be the same (verify) (I think this is false, TBD verify)
- in the `train_config.yml` at `pytorch-3dunet/resources/3DUnet_lightsheet_boundary/`, there are patch and stride shapes for train val loaders. They have to be the same (verify)
have - patch shape's dimensions z, y, x each has to be the same multiple of the stride shape's z, y, x, respectively

This dataset's (dataset02) min and max resolutions:

- min zyx: 109, 1036, 253
- max zyx: 147, 1169, 414

Study of patch and stride shapes:  
```bash
# all patch shape dimensions >64
# all stride shape dimensions are less than half of the patch shapes'
# train patch shape yx are different than the val patch shape yx
# train patch shape y different than x
# val patch shape y different than x (80, 250, 100 train patch, 80, 240, 120 val patch, 20, 40, 40 stride (never different between train and val))
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
    ...
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 662, in _output_padding
        raise ValueError((
    ValueError: requested an output size of torch.Size([10, 12, 31]), but valid sizes range from [9, 11, 29] to [10, 12, 30] (for an input of torch.Size([5, 6, 15]))

# additional change: make val patch shape the same as train patch shape (80, 250, 100 both patches, 20, 40, 40 stride)
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
    ...
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 662, in _output_padding
        raise ValueError((
    ValueError: requested an output size of torch.Size([10, 12, 31]), but valid sizes range from [9, 11, 29] to [10, 12, 30] (for an input of torch.Size([5, 6, 15]))
    # (identical error message)

# additional change: make x, y the same in patch shape (80, 100, 100 patch and 20, 40, 40 stride)
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
    ...
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 662, in _output_padding
        raise ValueError((
    ValueError: requested an output size of torch.Size([20, 25, 25]), but valid sizes range from [19, 23, 23] to [20, 24, 24] (for an input of torch.Size([10, 12, 12]))

# additional change: make patch shape's z, y, x each be 4 times as big as stride shapes (80, 160, 160 patch and 20, 40, 40 stride)
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml
    ...
    2023-07-10 11:27:08,807 [MainThread] INFO UNetTrainer - eval_score_higher_is_better: False
    2023-07-10 11:27:20,625 [MainThread] INFO UNetTrainer - Training iteration [1/150000]. Epoch [0/999]
    2023-07-10 11:27:22,633 [MainThread] INFO UNetTrainer - Training iteration [2/150000]. Epoch [0/999]
    2023-07-10 11:27:23,124 [MainThread] INFO UNetTrainer - Training iteration [3/150000]. Epoch [0/999]

# --------------------------
# attempts from 230713-0:

# - factor of 5 between patch shape and stride shape did not work (same torch.Size([]) error message. Idea: maybe the ratio of z,y,x lengths within patch shape &/ within stride shape matter, too (keep in mind, not act on it yet).
# - when input data is of varying size, formulas: patch_shape = resolution - 2, stride_shape = 1,1,1 might work, but take very long to load. This is not an option

# patch=[60,600,120], stride=[20,200,40]
train3dunet ... (same multichannel data (scaled0.25,labeluint16,autofluorgb24, etc.) used )
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 662, in _output_padding
        raise ValueError((
    ValueError: requested an output size of torch.Size([7, 15, 75]), but valid sizes range from [5, 13, 73] to [6, 14, 74] (for an input of torch.Size([3, 7, 37]))

# --------------------------
# attempts from 230714-0:

# duplicate the stdout to a file (but still print it to stdout, thus duplicating it):
# runs 'command' normally, prints output to stdout (...or stderr - also console output) normally, duplicates stdout and stderr output to 'output.file', -a for 'append or create if empty/new file'
<command> 2>&1 | tee -a output.file

# take working values patch=[80,160,160], stride=[20,40,40], keep their ratio (which is 4) and increase the size of each shape proportionally
# preliminary stuff
ssh
tmux
srun --pty -n 1 -c 8 --mem=32G --gres=gpu:V100 --constraint=GPUMEM32GB --time=24:00:00 bash -l
screen -S 3dunet-230714-0-patch_ratio4
cd ~/data/cloud
bash pull-script.sh
bash createDirs.sh
tensorboard --logdir ~/data/cloud/chpts/chpt-230714-0/
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230714-0/nvidia-smi.log &

train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230714-0-ratio4.yml 2>&1 | tee -a ~/data/cloud/chpts/chpt-230714-0/console.output
    ...
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 662, in _output_padding
        raise ValueError((
    ValueError: requested an output size of torch.Size([12, 25, 25]), but valid sizes range from [11, 23, 23] to [12, 24, 24] (for an input of
    torch.Size([6, 12, 12]))

# change the ratio patch/stride from 4 to 3, making bigger patches possible, because the z resolution is smaller than x and much smaller y resolution.

# ------------------------------
# attempts from 230718:
# from now (date in folder names...) on:  train3dunet stdout & stderr output saved to a file in the output chpt folder (~/data/outputs/)

# tmux session 0

# chpt-230718-0
# follow previous troubleshooting notes from Thomas (patch and stride shape are the same, and they are powers of 2 (2^3), because 3dunet does 3 pooling steps (reduction in resolution))
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-230718-0-2tothe3patches.yml 2>&1 | tee -a ~/data/outputs/chpt-230718-0/console.output
    ...
    2023-07-18 11:25:07,750 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 288, 288], 'stride_shape': [80, 288, 288], 'threshold': 0.6, 'slack_acceptance': 0.01}
    2023-07-18 11:25:09,387 [MainThread] ERROR HDF5Dataset - Skipping train set: /home/dwalth/scratch/datasets/babb03/ct3/-crop-bicubic-scaled0.25/raw_RGB24-czyx-label_uint16/train/id03-img_Ch638nm-crop-scaled0.25-label-blur3D1-Otsu570-largest-uint16-h5.h5
    Traceback (most recent call last):
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/hdf5.py", line 142, in create_datasets
        dataset = cls(file_path=file_path,
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/hdf5.py", line 179, in __init__
        super().__init__(file_path=file_path, phase=phase, slice_builder_config=slice_builder_config,
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/hdf5.py", line 65, in __init__
        slice_builder = get_slice_builder(self.raw, self.label, self.weight_map, slice_builder_config)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 176, in get_slice_builder
        return slice_builder_cls(raws, labels, weight_maps, **config)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 158, in __init__
        raw_slices, label_slices = zip(*filtered_slices)
    ValueError: not enough values to unpack (expected 2, got 0)
    2023-07-18 11:25:09,413 [MainThread] INFO HDF5Dataset - Loading train set from: /home/dwalth/scratch/datasets/babb03/ct3/-crop-bicubic-scaled0.25/raw_RGB24-czyx-label_uint16/train/id07-img_Ch638nm-crop-scaled0.25-label-blur3D1-Otsu570-largest-uint16-h5.h5...
    2023-07-18 11:25:10,025 [MainThread] INFO Dataset - Slice builder config: {'name': 'FilterSliceBuilder', 'patch_shape': [80, 288, 288], 'stride_shape': [80, 288, 288], 'threshold': 0.6, 'slack_acceptance': 0.01}
    2023-07-18 11:25:10,025 [MainThread] ERROR HDF5Dataset - Skipping train set: /home/dwalth/scratch/datasets/babb03/ct3/-crop-bicubic-scaled0.25/raw_RGB24-czyx-label_uint16/train/id07-img_Ch638nm-crop-scaled0.25-label-blur3D1-Otsu570-largest-uint16-h5.h5
    Traceback (most recent call last):
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/hdf5.py", line 142, in create_datasets
        dataset = cls(file_path=file_path,
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/hdf5.py", line 179, in __init__
        super().__init__(file_path=file_path, phase=phase, slice_builder_config=slice_builder_config,
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/hdf5.py", line 65, in __init__
        slice_builder = get_slice_builder(self.raw, self.label, self.weight_map, slice_builder_config)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 176, in get_slice_builder
        return slice_builder_cls(raws, labels, weight_maps, **config)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 139, in __init__
        super().__init__(raw_dataset, label_dataset, weight_dataset, patch_shape, stride_shape, **kwargs)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 59, in __init__
        self._raw_slices = self._build_slices(raw_dataset, patch_shape, stride_shape)
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 107, in _build_slices
        for x in x_steps:
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 120, in _gen_indices
        assert i >= k, 'Sample size has to be bigger than the patch size'
    AssertionError: Sample size has to be bigger than the patch size
# some datasets are too small for the given patch shape (288 in y is too big)

# 230718-1
# patch = stride = [96,240,240]
# CHECK: patch shape is smaller than all samples' size
# ERROR: with patch shape = stride shape (& this specific shape (unknown, at this point, if that makes a difference)):
    # "ValueError: not enough values to unpack (expected 2, got 0)"
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-230718-1-<description>.yml 2>&1 | tee -a ~/data/outputs/chpt-230718-1/console.output
    ...
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 158, in __init__
        raw_slices, label_slices = zip(*filtered_slices)
    ValueError: not enough values to unpack (expected 2, got 0)
        # This is the error when patch shape = stride shape (& with shape as big as it is, now)

# 230718-1-0
# patch != stride
# patch + 1*stride <= min-resolution
# patch = [96,240,240], stride = [8,8,8]
# => VALID PARAMETERS
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/outputs/chpt-230718-1-0/nvidia-smi.log &
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230718-1-0-patch[96,240,240],stride[8,8,8].yml 2>&1 | tee -a ~/data/outputs/chpt-230718-1-0/console.output
    ...
    <training is working>
    <train loss is decreasing>
    # letting it run until srun times out
squeue -s -u dwalth
            STEPID     NAME PARTITION     USER      TIME NODELIST
        4100212.0     bash  standard   dwalth   3:40:47 u20-computeibmgpu-vesta8
    4100212.extern   extern  standard   dwalth   3:40:47 u20-computeibmgpu-vesta8
    4103392.batch    batch  standard   dwalth     22:16 u20-compute-m1
    4103392.extern   extern  standard   dwalth     22:16 u20-compute-m1

# 230718-2
# patch = stride = [48,112,112]
# patch + 1*stride <= min-resolution (aka res_min)
# patch number is mostly 2, 1 in case of id02 data set (unclear, why)
# => VALID PARAMETERS
# => no train loss - cancelled the train3dunet process
tensorboard --logdir ~/data/outputs/chpt-230718-2/
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/outputs/chpt-230718-2/nvidia-smi.log &
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230718-2-patch[48,112,112],stride[48,112,112].yml 2>&1 | tee -a ~/data/outputs/chpt-230718-2/console.output
    ...
    <training is working>
    <train loss is constant (patches must have missed the region of the heart (the only label in the label images))>

# tmux attach -t 3

# 230718-3
# patch != stride
# patch + 1*stride <= res_min
# optimization: res_max >= patch + x_small * stride
    # where x_small is optimized for begin small, i.e., biggest input images do not have many more patches than the smallest input images
    # optimized dimension-wise
# optimization: patch >= stride
# optimization: patch big (close to res_min)
srun --pty -n 1 -c 8 --mem=32G --gres=gpu --time=24:00:00 bash -l
nvidia-smi --list-gpus
    GPU 0: Tesla V100-SXM2-16GB (UUID: GPU-3e262d5d-0626-9183-de73-27b629371d47)
screen -S <3dunet-date-$i>
tensorboard --logdir ~/data/outputs/chpt-230718-3/
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/outputs/chpt-230718-3/nvidia-smi.log &
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230718-3-patch[64,896,160],stride[32,128,80].yml 2>&1 | tee -a ~/data/outputs/chpt-230718-3/console.output
    ...
    <loaded successfully>
    <trains successfully>... wait
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 608, in _conv_forward
    return F.conv3d(
    torch.cuda.OutOfMemoryError: CUDA out of memory. Tried to allocate 1.09 GiB (GPU 0; 15.77 GiB total capacity; 14.28 GiB already allocated; 217.12 MiB free; 14.30 GiB reserved in total by PyTorch) If reserved memory is >> allocated memory try setting max_split_size_mb to avoid fragmentation.  See documentation for Memory Management and PYTORCH_CUDA_ALLOC_CONF
    # out of memory
# exit screen session
srun --pty -n 1 -c 8 --mem=32G --gres=gpu:V100 --constraint=GPUMEM32GB --time=24:00:00 bash -l
# recreate screen, etc.
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230718-3-patch[64,896,160],stride[32,128,80].yml 2>&1 | tee -a ~/data/outputs/chpt-230718-3/console.output
    ...
    <trains successfully>
    # VRAM usage is now 20GB (1 patch per data set (confusing as to why only 1 patch, but I'll accept it.))
    # let it run over night
    <tensorboard analytics>
        # train loss & eval score look good. train predictions, too.
        # val loss, eval score & predictions look bad (label not in loaded patch?)
        # => redo the cropping to ensure the label organ is in the patches of the different data sets.

# use this in future:
train3dunet --config <config_file_path> 2>&1 | tee -a ~/data/outputs/chpt-230718-3/train3dunet.output
```

attempt at deploying a well-trained model (I suppose well-trained, idk, let's see the segmentation results):
```bash
# 230719-0
# 230720-0 (try again, now the requested node is available)
ssh
tmux attach -t 0
srun --pty -n 1 -c 8 --mem=32G --gres=gpu:V100 --constraint=GPUMEM32GB --time=02:00:00 bash -l
    srun: job 4154413 queued and waiting for resources  # noting the job ID
    new try: 4157963
screen -S 3dunet-230720-0-test
module load anaconda3  # no tensorboard required when deploying a model, I think
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/outputs/test-230720-0/nvidia-smi.log &
predict3dunet --config <CONFIG> 2>&1 | tee -a ~/data/outputs/test-230719-0/predict3dunet.output
predict3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/test_config-230720-0.yml
    # with the same patch and stride shape as when training this particular model:
    ...
    Error with the torch.Size([]) requested, but valid ranges ...
# => TBD: crop all images to the same size and retry the train3dunet and predict3dunet from scratch.
```

### <u>Instructions on the ScienceCluster UZH</u>

The input data should be located on the cluster's scratch partition / drive.

Here is a page about the [resources of the ScienceCluster](https://docs.s3it.uzh.ch/cluster/resources/). Here is a sub page about the [resources of the A100 cards (& other hardware)](https://docs.s3it.uzh.ch/cluster/resources/#hardware) on the ScienceCluster - one A100 GPU has 80.0 GB VRAM, the V100 GPUs are available in flavours of 16.0 GB and 32.0 GB VRAM.

Running the command **`tensorboard --logdir <checkpoint/logs-0/>` is not necessary** for getting tensorboard statistics, because: The `train3dunet` command uses `train_config.yml` files which contain an argument called `checkpoint_dir`, or so. This directory is the one tensorboard takes as priority for exporting its training statistics to.

### <u>schematic workflow</u>

- get data from microscope
- input data formatting (to HDF5: autofluorescence: CZYX (uint8 works), label: ZYX (uint16 works))
- transfer data with globus
- adapt model parameters (paths, shapes, checkpoint folder, config yaml)
- adapt train_config.yml; make a copy & rename according to settings

```bash
train_config-230711-0-lower_patience.yml
/home/dwalth/data/cloud/chpts/chpt-230711-0/
jobid 4007175, step 0
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230711-0/nvidia-smi.log &
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230711-0-lower_patience.yml
```

- adapt shell commands (paths)
- git sync the files between PC and cluster
- run the shell commands

For more information on how to conduct scientific workflows regarding/with cloud / computing cluster computation, refer to the S3IT's dedicated gitlab repository [(Computational) "Scientific Workflows"](https://gitlab.uzh.ch/devin.routh/scientific-workflows) for this. Also refer to [my notes from taking their dedicated course](https://github.com/radRoy/MSc/tree/master/scientific-workflows%20notes) for this.

### <u>Example calculation of the patch and stride shapes (with differing image sizes between specimens)</u>

*Refer to a separate textfile for the resolutions of tha babb03-ct3 images (cropped, and scaled by 0.25, that is).*

specimen ID, z-resolutions, y-resolutions, x-resolutions
1, z, y, x
2, z, y, x
3, z, y, x
4, z, y, x
5, z, y, x
6, z, y, x
7, z, y, x

### <u>actual CLI usage when `ssh`-ing into the ScienceCluster UZH</u>

*For a short workflow for clumsily running several `train3dunet` commands simultaneously, on the same node (with `&`, putting something to background `bg` until it's complete), refer to the ~adjacent file "train_in_parallel.md".*

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
cd ~  # have to be in home directory to run `srun` commands
srun --pty -n 1 -c 8 --gres=gpu:A100 --mem=128G --time=24:00:00 bash -l
srun --pty -n 1 -c 8 --gres=gpu:V100 --mem=32G --time=24:00:00 bash -l
srun --pty -n 1 -c 16 --gres=gpu:T4 --mem=60G --time=24:00:00 bash -l
    # one T4 node has 16 cpus and 60G memory and 1 T4 GPU with 16.0 G VRAM
srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l

# requesting a specific V100 version
srun --pty -n 1 -c 8 --mem=32G --time=24:00:00 --gres=gpu:V100:1 --constraint=GPUMEM32GB bash -l
# equivalently
module load v100-32g
srun --pty -n 1 -c 8 --mem=32G --time=24:00:00 --gres=gpu bash -l

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
    # necessary for (at least live) tensorboard log output.
    # not necessary for train3dunet to run
tensorboard --logdir ~/data/cloud/chpts/chpt-230707-2/
tensorboard --logdir ~/data/outputs/chpt-230718-0/
# starting the GPU memory logging process (scientific-workflows) in the background (finishes when terminal session ends (endless loop))
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/outputs/chpt-230718-0/nvidia-smi.log &
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/outputs/chpt-230718-1/nvidia-smi.log &

tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230707-2/
# typical train3dunet execution command (inside an appropriate gpu compute session), and some alternatives
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml
# printing the output to stdout (nothing new), and duplicating it (incl. errors) to a file
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml 2>&1 | tee -a ~/data/outputs/chpt-230718-0/console.output
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml 2>&1 | tee -a ~/data/outputs/chpt-230718-1/console.output
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
screen -S 3dunet-230710-0-accum
srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=24:00:00 bash -l
squeue -s -u dwalth
            STEPID     NAME PARTITION     USER      TIME NODELIST
        4002322.0     bash  standard   dwalth      0:05 u20-computeibmgpu-vesta6
    4002322.extern   extern  standard   dwalth      0:05 u20-computeibmgpu-vesta6
nvidia-smi --list-gpus
    GPU 0: Tesla V100-SXM2-16GB (UUID: GPU-bad7e169-429d-f470-b499-9272ccc3d7ad)
cd ~/data/cloud/
bash createDirs.sh
    Created directory chpts/chpt-230710-0
module load anaconda3 tensorboard
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230710-0/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230710-0/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-accumulated.yml

<ctrl z>  # put train3dunet in background
<ctrl a d>  # detach screen session
screen -ls  # verify the screen session still exists

# try again with multi channel data but now with shapes that work with single channel data. (80, 160, 160 patches, 20, 40, 40 strides, both train and val shapes)
srun --pty -n 1 -c 8 --gres=gpu --mem=32G --time=24:00:00 bash -l
squeue -s -u dwalth
            STEPID     NAME PARTITION     USER      TIME NODELIST
        4002408.0     bash  standard   dwalth      1:07 u20-computeibmgpu-vesta7
    4002408.extern   extern  standard   dwalth      1:07 u20-computeibmgpu-vesta7
cd ~/data/cloud
bash createDirs.sh
    Created directory chpts/chpt-230710-1
module load anaconda3 tensorboard
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230710-1/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230710-1/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-RGB24raw,uint16label-230710-1-3in1out-shapeChange.yml

---------------------------------------------------------
did not try yet
---------------------------------------------------------
# session with only the 405 nm single channel data sets
screen -S 3dunet-230709-1-405
srun --pty -n 1 -c 8 --gres=gpu:T4 --mem=32G --time=24:00:00 bash -l
squeue -s -u dwalth
    #
cd ~/data/cloud
bash createDirs.sh
    Created directory chpts/chpt-230710-1
module load anaconda3 tensorboard
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230710-1/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230710-1/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-RGB24raw,uint16label-230710-1-3in1out-shapeChange.yml
    # successfully trains on the multichannel input data
# do not press CTRL + Z - this will pause the train3dunet command.
<CTRL + A + D>  # detach the screen session
screen -ls  # verify the screen still exists
```

## <u>Things to keep an eye on (e.g., potential or exposed bugs)</u>

1. When putting a computer on standby while a screen session is still attached, that screen session will be frozen when reconnecting from anywhere.

## <u>Documenting progress</u>

### <u>runs on 23.07.13 (meeting day) - improving train loss & eval score on multichannel data by increasing patch size</u>

The aim of this training is to find hyperparameters (specifically patch & stride shape) that cause the train loss and val eval score curves to look like the successful single channel training run from 23.05.09,10,11 (just before the meeting two months ago).

Whether running tensorboard before train3dunet or not does not affect the validity of the patch and stride shape. I shortly thought it does, but that is false. `train3dunet` *always* needs the sample size to be bigger than patch size (it would have been weird, otherwise, especially if an external command can change how train3dunet works internally).

```bash
ssh dwalth@login1.cluster.s3it.uzh.ch
tmux  # created tmux window 2
# tmux attach -t 2  # to reattach to this session after returning to workplace
srun --pty -n 1 -c 8 --mem=32G --time=24:00:00 --gres=gpu:V100:1 --constraint=GPUMEM16GB bash -l  # jobid.stepno = 4011170.0 (date: 230713)

screen -S 3dunet-230713-0-biggerpatch
module load tensorboard anaconda3
tensorboard --logdir ~/data/cloud/chpts/chpt-230713-0/

source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230713-0/nvidia-smi.log &
ps  # verify the nvidia-smi command actually works and is running (= is listed in this command's output)

train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230713-0-biggerpatch.yml
<CTRL + A + D>  # detach from this screen session
screen -ls  # verify the session was not accidentally terminated (CTRL + D is the command for session termination)
# running successfully
```

## <u>Debugging</u>

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

### <u>Wrangling with the Input Data Format (formatting HDF5 data sets) for data with multiple channels (3 autofluorescence laser lines), and the input parameters</u>

This was most relevant in the weeks around 19.06.2023 and 07.07.2023 (at least). It was solved on 10.07.2023:
- Fuse the single channel images into some RGB like form - RGB24 is sure to work (from experience during this time)
- Verify that the tif images are formatted in [C, z, y, x] and not [z, y, x, C] as would be the default in Fiji, for example
- 
Use my scripts to convert the autofluorescence images 

Now, a list of combinations of invalid input data formats and/or parameters with their according error messages:

- Error message when, presumably (currently uncertain what the input data & parameters where), 
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

- Error message when the input data format is not valid, e.g., when the raw channels in the h5 file are given as separate internal paths, for instance /raw/405, /raw/488, etc. instead of within one internal path /raw, like 3D U-Net requires the input data to be formatted (i.e., [C, Z, Y, X] in one image data saved in the h5's /raw internal path):
```bash
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-compositeData.yml
    .../hdf5.py, line 75
    ...
    File "/apps/opt/spack/linux-ubuntu20.04-x86_64/gcc-9.3.0/anaconda3-2023.03-1-emayrkyj4zgh57gt37ztn55cwzrrhstk/lib/python3.10/site-packages/h5py/_hl/group.py", line 330, in __getitem__
        raise TypeError("Accessing a group is done with bytes or str, "
    TypeError: Accessing a group is done with bytes or str,  not <class 'slice'>
```

- Error message when the patch and/or (&/) stride shape are not valid, e.g., when the order [z, y, x] was forgotten or the image resolution was mistaken to be bigger than it is:
```bash
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-sequenceData.yml
    ...
    File "/data/dwalth/pytorch-3dunet/pytorch3dunet/datasets/utils.py", line 120, in _gen_indices
        assert i >= k, 'Sample size has to be bigger than the patch size'
    AssertionError: Sample size has to be bigger than the patch size
    # Solution: adapt patch & stride shape to the downscaled resolution (downscaled images in fiji still have original xy res displayed, too (also the actual scaled res, of course))
```

```bash
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
The problem turned out to be the patch and stride shape, not the input data format. The input data format, here, is valid and works for 3D U-Net

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
    ...
    File "/home/dwalth/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 608, in _conv_forward
        return F.conv3d(
    RuntimeError: Given groups=1, weight of size [32, 1, 1, 1, 1], expected input[1, 3, 40, 100, 250] to have 1 channels, but got 3 channels instead
```

Therefore, specifying 3 input channels for the /raw hdf5 internal path with formatting (C,Z,Y,X) is correct (where C is 3 in this case).

## Know-How section (TBD)

The content in this section is, for example, know-how about bash handling.