Daniel Walther
creation date: 31.08.2023 (dd.mm.yyyy)

# <u>Study of patch and stride shapes</u>:  

## <u>dataset02 tests</u>

These tests range from about 230711 to 230718 (yymmdd). The used `train_config.yml` files were not all kept.

The list of used .yml config files:
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml`
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml`
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml`
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-singleChannels-405nm-fiji.yml`
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230714-0-ratio4.yml`
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-230718-0-2tothe3patches.yml`
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config-230718-1-<description>.yml`
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230718-1-0-patch[96,240,240],stride[8,8,8].yml`
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230718-2-patch[48,112,112],stride[48,112,112].yml`
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230718-3-patch[64,896,160],stride[32,128,80].yml` (out of memory)
- `~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230718-3-patch[64,896,160],stride[32,128,80].yml` (trains successfully)

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