"""
This file is for formatting hdf5 files the right way, so that 3D U-Net can handle the multi-channel images.
Fiji's default is to save RGB images in the order zyxC, but U-Net takes multi-channel input as Czyx.

From tif to hdf5.

Author: Daniel Walther
creation date: 2023.07.04
"""


#import h5py
#import matplotlib.pyplot as plt
import skimage
import numpy as np
import os.path
import fileHandling as fH


def reformat_tif_stack(tif_stack):

    # reading tiff z stack into a numpy.ndarray
    image = skimage.io.imread(tif_stack)

    # reformatting tiff z stack with np.rollaxis() from Fiji's RGB zyxC order to the 3D U-Net desired Czyx order
    image = np.rollaxis(image, 3, 0)  # 'rolling' the array with regard to its shape (shifting array's shape).
    #print(image.shape)
    
    print("reformat_tif_stack: image formatted")
    return image


def main(file, suffix):

    # if <'file' exists>
    if os.path.isfile(file):
        print("File", file, "exists and is a file.")

        image_formatted = reformat_tif_stack(file)
        file_out = fH.rename_file(file, suffix)
        fH.export_file(image_formatted, file_out)

        # TBD: put above stuff in a loop, reformatting all images in a given folder

        return 0

    # else
    print("File", file, "does not exist or is not a file. exit.")
    return 1


if __name__ == "__main__":
    
    # tif file with its data dimensions / order as such: [z, y, x, c], where zyx are image dimensions (pixel locations),
    # and c is channel (laser lines saved as RGB)
    tif_from_fiji = "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackRGB24/" \
                    "id01-Ch405,488,561nm-crop-scaled0.25-hyperstackRGB.tif"
    main(tif_from_fiji, "czyx")

    # test of error messages
    """folder_path = "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackRGB24/"
    main(folder_path, "ASDF")"""
