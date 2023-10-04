"""
daniel walther
creation date (dd.mm.yyyy): 03.10.2023
prupose: Scroll through the 15000 line long nvidia-smi log file containing logs for all runs of the day 230901,
    and extract the information I want from them (the VRAM usages & capacity),
    because I am too lazy to do it by hand.
    In hindsight, it probably would have been faster by hand, but whatever.

function: extract the max used VRAM for different runs from one collective nvidia-smi output log file.
    - take a nvidia-smi.log file containing the nvidia-smi outputs of multiple train3dunet runs and separate them.
    - calculate the maximum VRAM usage for each run.
    - (save it to a csv file.) => can just print things to stdout and manually transfer data to the 3dunet excel table.
"""


import sys
from typing import List


def process_nvidia_smi_line(line: str):
    """
    Extracts gpu name, used memory, free memory, and calculates memory capacity from a line of nvidia-smi.log output text.

    Args:
        line: str: A line from file.readlines() from a cloud/outputs/.../nvidia-smi.log file, e.g.: 'NVIDIA A100-SXM4-80GB, 0 MiB, 81052 MiB'.

    Returns: A tuple containing the given line's str variables for (gpu name, used memory, free memory, memory capacity).

    """

    """ TESTING
    print(f"process_nvidia_smi_line(line)'s line: '{line}'.")
    """

    split_line: list[str] = line.split(" ")
    gpu = split_line[0] + " " + split_line[1].strip(",")
    used = int(split_line[2])
    free = int(split_line[4])
    cap = used + free

    return gpu, used, free, cap


def main(arg="C:/Users/Dancer/Documents/cluster/data/outputs/chpt-230901-0/nvidia-smi.log"):
    """ OPEN FILE """

    with open(file=arg, mode="r") as file:

        # read the text into a list so it can be read multiple times
        readlines = file.readlines()
        lines = []
        for line in readlines:
            lines.append(line)

        """ TESTING
        # explore the text file
        n_lines = len(lines)
        for line in lines[0:2]:
            print(line, end="")
        print("")
        print(lines[2].split(" "))
        gpu = line.split(" ")[0] + " " + line.split(" ")[1].strip(",")
        used = int(line.split(" ")[2])
        free = int(line.split(" ")[4])
        print(type(gpu), gpu.strip(","))
        print(type(used), used)
        print(type(free), free)
        print("")
        """

        # put gpu name, used memory, and free memory in a pandas data frame // or in any or list format, doesn't matter
        columns = ("gpu", "memory_used_MiB", "memory_free_MiB")
        gpus = []
        mem_used_MiB = []
        mem_free_MiB = []
        mem_cap_MiB = []
        mem_cap_unique = []

        # first iteration (first line)
        # extract character values to variables
        gpu, used, free, cap = process_nvidia_smi_line(lines[1])
        # append variables to respective lists
        gpus.append(gpu)
        mem_used_MiB.append(used)
        mem_free_MiB.append(free)
        mem_cap_MiB.append(cap)
        # append unique memory capacity values to its respective list
        if cap not in mem_cap_unique:
            mem_cap_unique.append(cap)

        # print(f"last line:\n {lines[-1]}\n")
        # 'Tesla V100-SXM2'
        lines.pop(-1)
        # print(f"last line:\n {lines[-1]}\n")
        # 'Tesla V100-SXM2-32GB, 0 MiB, 32500 MiB'

        # all subsequent iterations (lines)
        for i, line in enumerate(lines[2:]):
            # extract character values to variables
            gpu, used, free, cap = process_nvidia_smi_line(line)
            # if this line does not contain the same values as the previous line
            if used != mem_used_MiB[-1]:
                # append variables to respective lists
                gpus.append(gpu)
                mem_used_MiB.append(used)
                mem_free_MiB.append(free)
                mem_cap_MiB.append(cap)
                # append unique memory capacity values to its respective list
                if cap not in mem_cap_unique:
                    mem_cap_unique.append(cap)

    """ FILE CLOSED """

    """ TESTING
    for i, cap_unique in enumerate(mem_cap_unique):
        print(f"gpu: {gpus[0]}\nunique cap {i}: {cap_unique}")
    print("")
    """

    # separating the max memory usages
    VRAM_gpu = []
    VRAM_usage = []
    VRAM_free = []
    VRAM_capacity = []
    # ... and counting the number of sessions contained in the given nvidia-smi.log file (depending on how 3dunet sessions are run, one log file can contain concatenated nvidia-smi outputs of multiple 3dunet sessions.
    n_0vram = 0
    usage_max = -1
    available_min = -1
    for i in range(len(gpus)):

        """ TESTING
        print(f"TESTING\t gpu: {gpus[i]}, mem_used_MiB: {mem_used_MiB[i]}, mem_free_MiB: {mem_free_MiB[i]}, mem_cap_MiB: {mem_cap_MiB[i]}")
        """

        usage = mem_used_MiB[i]
        available = mem_free_MiB[i]
        gpu_i = gpus[i]

        # assumes that during training, the nvidia-smi command was executed before the train3dunet command, therefore writing to the log file before anything was loaded into gpu memory (i.e., memory used is then always 0 in the first few lines of the log file).
        if usage == 0:

            # handling edge case where multiple lines contain 0 VRAM usage (i.e., the same run needed some time before starting to fill VRAM).
            if len(VRAM_usage) > 0:
                if usage == VRAM_usage[-1]:
                    continue

            # increasing counter of separate runs in this nvidia-smi log
            n_0vram += 1

            # handling/preparing max and min calculations, etc.
            usage_max = usage
            available_min = available
            VRAM_usage.append(usage_max)
            VRAM_free.append(available_min)

            VRAM_gpu.append(gpu_i)
            VRAM_capacity.append(usage_max + available_min)

        else:

            # handling edge case which should not occur if train3dunet & prep. steps are executed correctly.
            assert len(VRAM_usage) > 0, (f"\n Error: The list 'VRAM_usage' is empty (should not).\n Source problem: The first line in the give nvidia-smi.log file is not '0' for 'mem.used [MiB]'. Please review the file '{arg}' (e.g., just insert a line with 0 for mem.used). This means something went wrong when preparing &/ running train3dunet, most probably a user/developer error.")
            # this case automatically also handles the case where usage_max and available_min are not yet assigned a log value (i.e., they are -1). This should never happen, anyways, but I might forget something in the future and this point right here is very practical for checking for this mistake (i.e., invalid/absent contents of nvidia-smi.log file).

            # handling max and min calculations, etc.
            usage_max = max(usage, usage_max)
            available_min = min(available, available_min)
            VRAM_usage[-1] = usage_max
            VRAM_free[-1] = available_min

            VRAM_gpu[-1] = gpu_i
            VRAM_capacity[-1] = usage_max + available_min

    # handling the edge case, where the nvidia-smi.log file has '0' used VRAM. This can happen when experimenting with train3dunet in interactive slurm sessions.
    if mem_used_MiB[-1] == 0:
        n_0vram -= 1
        VRAM_usage.pop(-1)
        VRAM_free.pop(-1)
        VRAM_gpu.pop(-1)
        VRAM_capacity.pop(-1)

    for i, (gpu_j, vram_used, vram_free, vram_cap) in enumerate(zip(VRAM_gpu, VRAM_usage, VRAM_free, VRAM_capacity)):
        print(f"session {i}, gpu: {gpu_j}, mem_used_MiB: {vram_used}, mem_free_MiB: {vram_free}, mem_cap_MiB: {vram_cap}.")


if __name__ == "__main__":
    for a, arg in enumerate(sys.argv):
        print(f"argument {a}: {arg}")
        # the first element (index 0) in sys.argv is always the absolute file path of the current python script.

    if len(sys.argv) > 1:
        for i, arg in enumerate(sys.argv[1:]):
            print(f"\nnvidia-smi-separate_sessions.py: file {i} {arg}")
            main(arg)

    else:
        # for local (Dancer) testing with a default file, write "" as list element.
        # default file: "C:/Users/Dancer/Documents/cluster/data/outputs/chpt-230901-0/nvidia-smi.log"
        static_arguments = ["C:/Users/Dancer/Documents/cluster/data/outputs/chpt-230901-0/nvidia-smi.log", "C:/Users/Dancer/Documents/cluster/data/outputs/chpt-230905-1/nvidia-smi.log"]
        for i, arg in enumerate(static_arguments):

            if arg == "":
                print(f"\nnvidia-smi-separate_sessions.py: file {i} '{arg}'")
                main()

            else:
                print(f"\nnvidia-smi-separate_sessions.py: file {i} '{arg}'")
                main(arg)
