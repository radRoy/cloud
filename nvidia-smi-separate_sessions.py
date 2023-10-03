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


""" OPEN FILE """


print("")  # add a newline at start of script output
with open(file="C:/Users/Dancer/Documents/cluster/data/outputs/chpt-230901-0/nvidia-smi.log", mode="r") as file:

    # read the text into a list so it can be read multiple times
    readlines = file.readlines()
    lines = []
    for line in readlines:
        lines.append(line)

    # explore the text file
    n_lines = len(lines)
    for line in lines[0:2]:
        print(line, end="")
    print("")
    print(lines[2].split(" "))
    # gpu = line.split(" ")[0] + " " + line.split(" ")[1].strip("-")
    # used = int(line.split(" ")[2])
    # free = int(line.split(" ")[4])
    gpu = line.split(" ")[0] + " " + line.split(" ")[1].strip(",")
    used = int(line.split(" ")[2])
    free = int(line.split(" ")[4])
    print(type(gpu), gpu.strip(","))
    print(type(used), used)
    print(type(free), free)
    print("")

    # put gpu name, used memory, and free memory in a pandas data frame // or in any or list format, doesn't matter
    columns = ("gpu", "memory_used_MiB", "memory_free_MiB")
    gpus = []
    mem_used_MiB = []
    mem_free_MiB = []
    mem_cap_MiB = []
    mem_cap_unique = []

    # first iteration (first line)
    # extract character values to variables
    gpu = lines[1].split(" ")[0] + " " + lines[1].split(" ")[1].strip(",")
    used = int(lines[1].split(" ")[2])
    free = int(lines[1].split(" ")[4])
    cap = used + free
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
        #split_line = line.split(" ")
        gpu = line.split(" ")[0] + " " + line.split(" ")[1].strip(",")
        used = int(line.split(" ")[2])
        free = int(line.split(" ")[4])
        cap = used + free
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


for cap_unique in mem_cap_unique:
    print(f"gpu: {gpus[0]}\nunique cap: {cap_unique}")
print("")

n_0vram = 0
for i in range(len(gpus)):
    print(f"gpu:\t{gpus[i]},\tmem_used_MiB:\t{mem_used_MiB[i]},\tmem_free_MiB:\t{mem_free_MiB[i]},\tmem_cap_MiB:\t{mem_cap_MiB[i]}")
    if mem_used_MiB[i] == 0:
        n_0vram += 1
n_0vram -= 1  # at the end, the read nvidia-smi log has 0s, so subtracting this last count
print("")
print(f"n vram = 0: {n_0vram}")
    # the n of 0s at the start of an nvidia-smi log entry is 20, the same number of runs on that day (230901, all runs range from -0 to -19), and all these runs' nvidia log files are progressively and consistently smaller. All contain the same last lines.
print("")

# separating the max memory usages
max_usage = []
min_available = []
VRAM_usage = []
VRAM_free = []
for i in range(len(gpus)):
    usage = mem_used_MiB[i]
    avail = mem_free_MiB[i]

    if usage == 0:
        if i == 0:
            max_usage = [usage]
            min_available = [avail]
            continue
        # calc max and min for this run
        VRAM_usage.append(max(max_usage))
        VRAM_free.append(min(min_available))
        max_usage = [usage]
        min_available = [avail]

    else:
        max_usage.append(usage)
        min_available.append(avail)

for vram_used, vram_free in zip(VRAM_usage, VRAM_free):
    print(f"used: {vram_used}\nfree: {vram_free}")