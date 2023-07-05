import skimage
import os


def path_all_slash(file):

    # replacing "\" with "/" in the given filepath
    """file_out = ""
    for i in range(len(file)):
        if file[i] == "\\":
            file_out += "/"
        else:
            file_out += file[i]
    file_out

    return file_out"""

    return file.replace("\\", "/")


# TBD: CAUTION: Does not work
"""def path_all_backslash(file):

    # idea: could use os.path.normpath(file), forcing normpath() to convert to backslash
    # (i.e., making it think it is running on Windows (hopefully there's an input argument for that))

    # replacing "/" with "\" in the given filepath
    file = file.replace("/", "\\")  # creates double backslash where there is one slash
    return file.replace("\\\\", "\\")  # changes nothing since replacing <s> with '\\' writes double backslash'"""


def rename_file(file, suffix):
    """
    Renames a file by taking a filename including absolute path, adding a suffix to it and returning the resulting filename.
    Args:
        file: str, absolute path, handles '\' and '/'
        suffix: str,

    Returns: str, filename with the desired suffix appended to it, preceding file extension.
    """

    # replacing "\" with "/" in the given filepath
    file = path_all_slash(file)

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
    exit(0)
