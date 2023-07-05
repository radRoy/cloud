import tkinter as tk
from tkinter import filedialog
import skimage
import os


def rename_file(file, suffix):
    """
    Renames a file by taking a filename including absolute path, adding a suffix to it and returning the resulting filename.
    Args:
        file: str, absolute path, handles '\' and '/'
        suffix: str,

    Returns: str, filename with the desired suffix appended to it, preceding file extension.
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

    skimage.io.imsave(filename, image)  # , photometric='minisblack'

    print(image.shape)
    print("export_tif(): File created: {}".format(filename))
    return 0


if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    print(file_path)

    exit(0)
