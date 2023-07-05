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


def reformat_tif_stack(tif_stack):

    # reading tiff z stack into a numpy.ndarray
    image = skimage.io.imread(tif_stack)

    # reformatting tiff z stack with np.rollaxis() from Fiji's RGB zyxC order to the 3D U-Net desired Czyx order
    image = np.rollaxis(image, 3, 0)  # 'rolling' the array with regard to its shape (shifting array's shape).
    #print(image.shape)
    
    print("reformat_tif_stack: image formatted")
    return image


def rename_file(file, suffix):
    temp = file.split("/")
    dir_in = temp[-2]
    name_ext = temp[-1]

    # create the name of the output directory
    parent_dir = ""
    for dir_part in temp[:-2]:
        parent_dir += dir_part + "/"
    dir_suffixed = dir_in + "-" + suffix + "/"
    dir_out = parent_dir + dir_suffixed

    # creates the dedicated output directory if it doesn't exist
    os.mkdir(dir_out) if not os.path.exists(dir_out) else None

    # create the file_out name, including its full absolute path, added suffix and file extension
    names = name_ext.split(".")
    extension = names[-1]
    name = ""
    for part in names[:-1]:
        name += part + "."
    name = name.strip(".")
    name_out = name + "-" + suffix  # output filename without extension but with suffix describing processing operation
    name_out_ext = name_out + "." + extension
    file_out = dir_out + name_out_ext

    return file_out


def export_tif(image, filename):
    """
    Exports a numpy.ndarray (e.g., a tif z stack) to .tif format.
    Args:
        image: numpy.ndarray (e.g., a formatted RGB24 TIFF z stack)
        filename: filename preceded by the absolute path where it is to be saved

    Returns: nothing (0)

    """
    skimage.io.imsave(filename, image)  # , photometric='minisblack'

    print(image.shape)
    print("export_tif(): File created: {}".format(filename))
    return 0


def main(file, suffix):

    # if <'file' exists>
    if os.path.isfile(file):

        image_formatted = reformat_tif_stack(file)
        file_out = rename_file(file, suffix)
        export_tif(image_formatted, file_out)

        # TBD: put above stuff in a loop, reformatting all images in a given folder

        return 0

    # else
    print("File", file, "does not exist.")
    return 1


if __name__ == "__main__":
    
    # tif file with its data dimensions / order as such: [z, y, x, c], where zyx are image dimensions (pixel locations),
    # and c is channel (laser lines saved as RGB)
    tif_from_fiji = "M:/data/d.walther/Microscopy/babb03/tiff-ct3/-crop-bicubic-scaled0.25-autofluo-hyperstackRGB24/" \
                    "id01-Ch405,488,561nm-crop-scaled0.25-hyperstackRGB.tif"
    main(tif_from_fiji, "czyx")
        