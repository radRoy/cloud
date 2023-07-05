"""
This script is for creating HDF5 files (data sets) for training a 3D U-Net model.
It should take tif as input and create h5 files in the desired format. The plan is to offer different options.

Author: Daniel Walther
creation date: 2023.07.05
"""


import h5py


def open_h5(file_h5):
    # file_h5: str to an .h5 file including absolute path (stand
    h5 = h5py.File(file_h5)
    pass


def tif_to_h5(tif_RGB24_czyx):  # unclear (TBD), whether format order czyx or zyxc (or other) matters for h5 creation.
    pass


if __name__ == "__main__":
    file = "path & name"

    exit(0)
