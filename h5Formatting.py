"""
This file is for formatting hdf5 files the right way, so that 3D U-Net can handle the multi-channel images.
Fiji's default is to save RGB images in the order zyxC, but U-Net takes multi-channel input as Czyx.

From tif to hdf5.

Author: Daniel Walther
creation date: 2023.07.04
"""


import h5py
#import matplotlib.pyplot as plt
import skimage
import numpy as np
import os.path


def read_tif(tif_fiji_rgb):
    image = skimage.io.imread(tif_fiji_rgb)
    print("image:\n", image)
    print("image dimensions:\n", len(image[0]), np.shape(image))
    pass


if __name__ == "__main__":
    
    # tif file with its data dimensions / order as such: [z, y, x, c], where zyx are image dimensions (pixel locations), and c is channel (laser lines saved as RGB)
    tif_from_fiji = "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackRGB24/id01-img_Ch405,488,561nm-crop-scaled0.25-hyperstackRGB.tif"
    print(os.path.isfile(tif_from_fiji))  # returns True if file exists
    
    read_tif(tif_from_fiji)

    x = y = z = np.arange(0, 5, 1)
    #np.savetxt('test.out', x, delimiter=',')   # X is an array
    np.savetxt('test.out', (x,y,z))   # x,y,z equal sized 1D arrays