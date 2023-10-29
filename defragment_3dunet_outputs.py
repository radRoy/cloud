"""
Daniel Walther
creation date (dd.mm.yyyy): 27.10.2023

purpose:
Delete the 3dunet pytorch output files from a fragmented backup location.

implementation:
- Make file tree lists.
- Read the line wise.
- Compare unique 'events.out.tfevents.1682602560.u20-computeibmgpu-vesta11.2759083.0' lines that are contained only in one of two files.
- Always compare a fragment with a reference file.
- Write only the unique 'events.out.tfevents...' log file names to a file with a similar name as the base file for the current unique log file name list. Start with the reference file tree text file 'outputs-file_tree-231027--1-cluster-data_outputs.txt', at the time of writing this program.
- The location of the files is 'C:/Users/Dancer/Documents/cloud/'.

special:
Run this program in the pycharm project "Documents" until I wrote a comprehensive suite of all my MSc related programs.
"""


import string  # python Lib/string.py, doc: https://github.com/python/cpython/blob/3.12/Lib/string.py, for punctuation detection
import tkinter as tk

import numpy as np

# This program must be run by first opening this projects parent folder "Documents" as a pycharm project. How this works in the MSc thesis end product is unclear, currently.
import imageProcessTif.fileHandling as fH


def extract_unique_log_names_from_text_file(file_path):

    with open(file_path, "r") as f:
        lines = ""
        for line in f.readlines():
            for char in line:
                if char.isalnum() or char in string.punctuation or char.isspace():
                    lines = lines + char if char not in ("\n", "%") else lines
    f.close()

    logs = []
    line_fragments = lines.split(" ")
    for fragment in line_fragments:
        if fragment.startswith("events.out.tfevents."):
            logs.append(fragment)

    return np.unique(logs)


def export_unique_logs_to_file_from_text_file(file_path):

    unique_logs = extract_unique_log_names_from_text_file(file_path)

    pass


if __name__ == "__main__":

    # tell python / tkinter explicitly to initialise the window creation process (and hide the init window)
    root = tk.Tk()
    root.withdraw()

    file_paths = fH.get_file_path_list()  # have to choose folder if called without input arguments like this.
    file_paths = fH.get_string_list_filtered_by_wanted_substring(l=file_paths, s="file_tree")
    file_paths = fH.get_string_list_filtered_by_unwanted_substring(l=file_paths, s=",")
    fH.iterate_function_args_over_iterable(file_paths, print)

    logs_0 = extract_unique_log_names_from_text_file(file_paths[0])
    print(logs_0)
