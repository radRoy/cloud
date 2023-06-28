daniel walther
creation date: 05.06.2023

sources:
- [This S3IT singularity tutorial](https://docs.s3it.uzh.ch/cluster/singularity_tutorial/)
- [dockerhub page of tensorflow's official docker image](https://hub.docker.com/r/tensorflow/tensorflow)

```bash
ssh dwalth@login1.cluster.s3it.uzh.ch
screen -S singularityWorkflow
screen -ls
    There are screens on:
            3121107.singularityWorkflow     (06/05/23 15:16:13)     (Attached)
            3035365.reInstall3dUnet (06/05/23 13:07:37)     (Detached)
            3032820.tbLogdirNotGiven        (06/05/23 13:03:50)     (Detached)
    3 Sockets in /run/screen/S-dwalth.
module load singularityce
cd data
# Pull the image directly from DockerHub
singularity pull docker://tensorflow/tensorflow
ls -hal
    total 494M
    drwx------   8 dwalth dwalth    7 Jun  5 15:19 .
    drwxr-xr-x 678 root   root    677 Jun  5 15:07 ..
    drwxrwsr-x   4 dwalth dwalth    2 Feb 28 15:27 conda
    drwxrwxr-x   2 dwalth dwalth    3 Mar 31 21:56 history_bashs
    drwxrwxr-x  14 dwalth dwalth   18 Mar 31 14:00 pytorch-3dunet
    drwxrwxr-x   7 dwalth dwalth   14 May 31 11:56 scientific-workflows
    -rwxrwxr-x   1 dwalth dwalth 494M Jun  5 15:19 tensorflow_latest.sif  # just downloaded this file
    drwxrwxr-x   2 dwalth dwalth    0 Jun  5 13:02 tmp
    drwxrwxr-x   5 dwalth dwalth    3 May 15 09:51 wolny

# Unpack a Singularity Image file (.sif) into a sandbox directory:
singularity build --sandbox sandbox_tf_latest tensorflow_latest.sif
    INFO:    Starting build...
    INFO:    Verifying bootstrap image tensorflow_latest.sif
    WARNING: integrity: signature not found for object group 1
    WARNING: Bootstrap image could not be verified, but build will continue.

    INFO:    Creating sandbox directory...
    INFO:    Build complete: sandbox_tf_latest
singularity shell -B /data -B /scratch -B /shares --nv sandbox_tf_latest
    WARNING: underlay of /usr/bin/nvidia-smi required more than 50 (452) bind mounts
Singularity> ls
    conda  history_bashs  pytorch-3dunet  sandbox_tf_latest  scientific-workflows  tensorflow_latest.sif  tmp  wolny
Singularity> nvidia-smi
    NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver. Make sure that the latest NVIDIA driver is installed and running.
Singularity> exit
exit
screen -ls
    There are screens on:
            3035365.reInstall3dUnet (06/05/23 13:07:37)     (Detached)
            3032820.tbLogdirNotGiven        (06/05/23 13:03:50)     (Detached)
    2 Sockets in /run/screen/S-dwalth.
```

