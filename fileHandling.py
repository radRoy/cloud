#import tkinter as tk
from tkinter import filedialog
import skimage
import os
import pathlib


def rename_file(file, suffix):
    """
    Renames a file by taking a filename including absolute path, adding a suffix to it and returning the resulting filename.

    Args:
        file: str, filename with extension, e.g., "file.png" (no preceding path)
        suffix: str, to be appended to the input filename (no separators like `-`, e.g., "file-suffix.png")

    Returns: str, filename with appended suffix followed by the input's file extension (no preceding path)

    """

    # creating a list of directories to extract certain partial directories and the filename
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

    skimage.io.imsave(filename, image)

    print(image.shape)
    print("export_tif(): File created: {}".format(filename))

    return 0


if __name__ == "__main__":

    """
    # tell python / tkinter explicitly to initialise the window creation process (and hide the init window)
    root = tk.Tk()
    root.withdraw()
    """

    exit(0)
