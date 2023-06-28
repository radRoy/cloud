Daniel Walther
creation date: 31.05.2023

## code / commands
cmd.exe:
```bash
ssh dwalth@login2.cluster.s3it.uzh.ch
cd ~/data
git clone https://gitlab.uzh.ch/devin.routh/scientific-workflows
cd scientific-workflows/
module load anaconda3
conda env create -f environment.yml
conda env list  # to see the environments
    # conda environments:
    #
    base                     /apps/opt/spack/linux-ubuntu20.04-x86_64/gcc-9.3.0/anaconda3-2022.10-4zvvyfdmb3tw45xdxcy7vcuhn5nw2s3i
    envWolny                 /home/dwalth/data/conda/envs/envWolny
    pytorch3dunet            /home/dwalth/data/conda/envs/pytorch3dunet
    tfbenchmark              /home/dwalth/data/conda/envs/tfbenchmark
# tfbenchmark was just created
```

singularity
```bash
cd ~/data/scientific-workflows/
ls -hal
    ...
    -rw-rw-r-- 1 dwalth dwalth  267 May 31 11:47 singularity.def
    ...
sudo singularity build tfbenchmark.sif singularity.def
    # does not work.
    # refer to the s3it singularity tutorial (linked in the workflows README)
```

[cluster singularity tutorial](https://docs.s3it.uzh.ch/cluster/singularity_tutorial/):  
...  
"For example, if you would like to acquire the latest GPU-compatible container version of TensorFlow, you would run the following code on ScienceCluster:"

still on the same login node
```bash
# Load the necessary modules in the cluster
module load singularityce
# Change to the /data directory
cd data  # or: cd ~/data
# Pull the image directly from DockerHub
singularity pull docker://tensorflow/tensorflow
    ...
    INFO:    Creating SIF file...
    FATAL:   While making image from oci registry: error fetching image to cache: while building SIF from layers: while creating squashfs: create command failed: exit status 1: FATAL ERROR: Out of memory (cache_alloc)
    # same
```
Circumvent the memory problem by building the singularity image from an interactive session (the result is data stored on data drive, regardless of the machine used):
```bash
# still in ~/data
srun --pty -n 1 -c 2 --time=01:00:00 --mem=16G bash -l
 squeue -s -u dwalth
            STEPID     NAME PARTITION     USER      TIME NODELIST
        1518259.0     bash  standard   dwalth      0:18 u20-compute-m5
    1518259.extern   extern  standard   dwalth      0:18 u20-compute-m5
singularity pull docker://tensorflow/tensorflow
    ...
    INFO:    Creating SIF file...
    # succeeded (just ended)
ls  # in ~/data
conda  history_bashs  pytorch-3dunet  scientific-workflows  tensorflow_latest.sif  tmp  wolny
    # tensorflow_latest.sif is there, now the building of it...
# MISSING COMMANDS
# <trying to build the singularity container>
# <fail for some reason>
# MISSING COMMANDS
scancel -u dwalth  # only needed the RAM for the image downloading
    srun: Force Terminated job 1518259
```