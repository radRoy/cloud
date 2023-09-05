# <u>cloud</u>

`tmux` essentials:
```bash
# new
tmux
# list
tmux list-sessions
# attach
tmux attach -t 0  # attaches to tmux session (='window') 0
# detach (press keys)
<CTRL + B> <D>
# kill
tmux kill-session -t 0  # when outside session 0
```

`screen` essentials:
```bash
# new
screen -S 3dunet
# list
screen -ls
# attach
screen -r 3dunet
# detach (press keys)
<CTRL+A> <D>
# kill
<CTRL + D>  # inside the screen session to be killed
```

~`slurm` essentials:
```bash
# interactive cluster gpu session
srun --pty -n 1 -c 4 --mem=8G --gres=gpu --constraint=GPUMEM32GB --time=24:00:00 bash -l
# cancelling a running slurm job
scancel -u dwalth  # cancels all running jobs of that user
scancel 4651350  # where 4651350 is job_id
# viewing a user's jobs
squeue -u dwalth  # can use the returned job_id for scancel
squeue -s -u dwalth  # also shows step number of each job id (e.g., when a job has multiple tasks/sub jobs or so)
squeue -u dwalth -i 5  # squeue request sent every 5 seconds
```

bash essentials:
```bash
# assigning a variable in-line in a bash shell (takes as string, I think)
today=230829-0
checkdir=~/data/outputs/chpt-230829-0

# duplicate the stdout to a file (but still print it to stdout, thus duplicating it):
# runs 'command' normally, prints output to stdout (...or stderr - also console output) normally, duplicates stdout and stderr output to 'output.file', -a for 'append or create if empty/new file'
<command> 2>&1 | tee -a output.file
```

other useful commands
```bash
# name of the gpu
nvidia-smi --list-gpus
    # GPU 0: Tesla V100-SXM2-16GB (UUID: GPU-3e262d5d-0626-9183-de73-27b629371d47)

# copy stdout to a file with 'tee'. file named after running command (instead of 'console.output')
train3dunet --config <config_file_path> 2>&1 | tee -a <checkpoint_dir>/train3dunet.output

# slurm session stuff
squeue -s -u dwalth -i 5
    # displays updated output every -i 5 seconds
squeue -s -u dwalth
    # $JOBID.stepno  # need both ID & stepno to attach to this node from another node
# attach to an existing slurm session
sattach $JOBID.$stepno
    # insert values from squeue output
```

## <u>Installation commands</u>

```bash
srun --pty -n 1 --time=8:00:00 --gres gpu:1  --mem=11G bash -l  # good idea to build environments on nodes it is intended for
ssh dwalth@login1.cluster.s3it.uzh.ch
module load anaconda3
conda create -n 3dunet
source activate 3dunet
conda install pip
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118  #
git clone https://github.com/wolny/pytorch-3dunet ~/data/pytorch-3dunet
pip install -e ~/data/pytorch-3dunet/
pip install pyyaml
pip install h5py
pip install tensorboard
pip install scikit-image
train3dunet
    # usage: train3dunet [-h] --config CONFIG
    # train3dunet: error: the following arguments are required: --config
# DW: Success.

## verify that cuda works  (should return 1; 0; True; some version (for record keeping in case sth. breaks in the future))
python << EOF 
import torch
print(torch.cuda.device_count())
print(torch.cuda.current_device())
print(torch.cuda.is_available())
print(torch.__version__)
EOF
    # output: 1, 0, True
    # torch version as of 28.08.2023: 2.0.1+cu118  (v2.0 seems to work compared to v1.12...)
# DW: Success.
conda env export > 3dunet.yml

# config files, etc. were configured previously (230821)
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230821-0-dataset03-testing-patch\[64\,896\,160\]-stride\[32\,128\,80\].yml
    # ran out of VRAM during the first training iteration - so the right resources are used and the installation works.
```

## <u>Usage of pytorch-3dunet</u>

### <u>Instructions on the `train_config.yml` files</u>

U-Net can only handle absolute paths. Therefore, when specifying paths on the cluster, e.g., when writing the new .yml file, **substitute `/~/` with `/home/dwalth/`**. For example:  
The path `/~/scratch/datasets/imaging03/scaled0.5/train` is invalid.  
The path `/home/dwalth/scratch/datasets/imaging03/scaled0.5/train` is valid.

However, when giving the config location to the `train3dunet` command, symbolic links with `~` work (bash):
```bash
train3dunet --config ~/data/pytorch-3dunet/resources/3DUnet_lightsheet_boundary/train_config.yml
```

### <u>`train3dunet` commands</u>

```bash
ssh ...
tmux
module load a100
#module load v100-32g
srun --pty -n 1 -c 6 --mem=32G --gres=gpu:1 --time=12:00:00 --mail-type=BEGIN,END,FAIL --mail-user=daniel.walther@uzh.ch bash -l
cd ~/data/cloud
today=230905
screen -S 3dunet-$today-0
bash pull-script.sh
bash createChptDirs.sh
#checkdir=~/data/outputs/chpt-230830-0  # assign in-line on cluster from 'bash createChptDirs.sh'
#session=230830-0  # assign in-line on cluster from 'bash createChptDirs.sh'

module load anaconda3
source activate 3dunet
tensorboard --logdir $checkdir
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f $checkdir/nvidia-smi.log &
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-$session.yml 2>&1 | tee -a $checkdir/train3dunet.output
# screen detach: <ctrl + a> <d>
# verify 'train3dunet' is running
top -u dwalth
# tmux detach: <ctrl + b> <d>
# verify slurm session is running
squeue -u dwalth
# cluster logout: <ctrl + d>
```




***<u>ALL ABOVE IS ORDERED. ALL BELOW IS NOT.</u>***




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