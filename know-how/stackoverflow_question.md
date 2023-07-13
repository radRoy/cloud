# stackoverflow post (my question) about input data formatting

## Question title

How should I format the HDF5 Input Data Sets when training 3D U-Net for semantic segmentation of organs from fluorescence lightsheet microscopy?

## Question body

**My data**:  
The image data I have was taken with a [mesoSPIM](https://mesospim.org/) (a meso-scale selective plane illumination microscope), which is a type of lightsheet microscopy.  
I have 4 excitation laser channels, meaning that I have 4 images (4 channels, or colors) of each specimen of my model organism. One of these channels is the fluorescence channel that's known to work properly. This is the channel used to make the labels (annotations). The other 3 channels are used for training data.

**The model I want to train**:  
3D U-Net for semantic segmentation of whole organs. I want to give 3 input channels (/raw HDF5 internal path) and 1 output, or target, channel (/label HDF5 internal path). The segmentation results should be the same for all the input channels.

**The problem I encounter**:  
When training each channel separately, training the model works well. However, when attempting to train on multi-channel input data, hoping for better results since the model has something like color-vision, so to speak, none of the Input Data Formats I tried have worked so far, with various error messages. Some error messages appear more often than others.

There are **two error messages I'm stuck with**, depending on how I attempt to format the input data sets.

1. error message:
```
train3dunet --config <config file path (train_config.yml)>
  ...
  # loading works fine
  ...
  # just before the 1st training iteration:
    traceback ...
    ...
    File "/data/<user>/pytorch-3dunet/pytorch3dunet/datasets/hdf5.py", line 97, in __getitem__
        label_patch_transformed = self.label_transform(self.label[label_idx])
    File "/data/<user>/pytorch-3dunet/pytorch3dunet/augment/transforms.py", line 21, in __call__
        m = t(m)
    File "/data/<user>/pytorch-3dunet/pytorch3dunet/augment/transforms.py", line 323, in __call__
        assert m.ndim == 3
    AssertionError
```

2. error message:
```
train3dunet --config <config file path (train_config.yml)>
  ...
  # loading works fine
  ...
  2023-07-07 13:55:14,898 [MainThread] INFO UNetTrainer - Training iteration [1/150000]. Epoch [0/999]
    Traceback (most recent call last):
    File "/home/<user>/local/bin/train3dunet", line 33, in <module>
        sys.exit(load_entry_point('pytorch3dunet', 'console_scripts', 'train3dunet')())
    ...
    File "/home/<user>/.local/lib/python3.10/site-packages/torch/nn/modules/conv.py", line 662, in _output_padding
    raise ValueError((
  ValueError: requested an output size of torch.Size([5, 12, 31]), but valid sizes range from [3, 11, 29] to [4, 12, 30] (for an input of torch.Size([2, 6, 15]))
```