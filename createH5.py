"""
This script is for creating HDF5 files (data sets) for training a 3D U-Net model.
It should take tif as input and create h5 files in the desired format. The plan is to offer different options.

notes, links:
- https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser for expanding ~/... to /home/user/...

Author: Daniel Walther
creation date: 2023.07.05
"""


import h5py
import fileHandling as fH


def open_h5(file_h5):
    # file_h5: str to an .h5 file including absolute path (stand
    h5 = h5py.File(file_h5, "r")
    return h5


def tif_to_h5(tif_RGB24_czyx):  # unclear (TBD), whether format order czyx or zyxc (or other) matters for h5 creation.
    pass


if __name__ == "__main__":

    path = fH.get_directory_dialog()
    files = fH.get_file_list(path)
    file_paths = [path + "/" + file for file in files]
    f = open_h5(file_paths[0])
    print(list(f.keys()))

    exit(0)
