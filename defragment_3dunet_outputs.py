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
from tqdm import trange

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

    return np.unique(logs)  # np.ndarray of a string list


def export_unique_logs_to_file_from_text_file(unique_logs: np.ndarray[str], export_path: str):
    with open(export_path, "w") as g:
        for log in unique_logs:
            g.write(log)
            g.write("\n")
    g.close()
    return None


def main():

    # tell python / tkinter explicitly to initialise the window creation process (and hide the init window)
    root = tk.Tk()
    root.withdraw()

    # input and output file paths
    input_paths = fH.get_file_path_list()  # have to choose folder if called without input arguments like this.
    input_paths = fH.get_string_list_filtered_by_wanted_substring(l=input_paths, s="file_tree")
    input_paths = fH.get_string_list_filtered_by_unwanted_substring(l=input_paths, s=",")
    print(f"\ninput paths:")
    fH.iterate_function_args_over_iterable(input_paths, print)
    output_paths = fH.get_output_from_input_file_path_list_and_suffix(input_paths, suffix="-unique_logs")
    print(f"\noutput paths:")
    fH.iterate_function_args_over_iterable(output_paths, print)

    # logs_0 = extract_unique_log_names_from_text_file(input_paths[0])

    reference_logs = extract_unique_log_names_from_text_file(file_path=input_paths[0])  # assumes that the file containing the reference logs file tree is the first in the ascendingly sorted file path list
    # - - -
    # hier stehengeblieben
    # - - -

    print("\n")
    for i_file, (file_path, export_path) in enumerate(zip(input_paths, output_paths)):
        print(f"main: Opening file no. {i_file}: {file_path}")
        unique_logs = extract_unique_log_names_from_text_file(file_path)

    print("\n")
    for export_path in output_paths:
        export_unique_logs_to_file_from_text_file(unique_logs, export_path)
        print(f"main: Wrote to file {export_path}")


if __name__ == "__main__":
    main()  # lets choose folder, reads all file_tree...txt files, exports unique log names compared to reference tree file.
