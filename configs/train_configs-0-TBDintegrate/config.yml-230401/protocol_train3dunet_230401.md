# commands protocol: pytorch 3d unet `sbatch` slurm job script
author: Daniel Walther
creation date: 2023.04.01
slurm submission date: 2023.04.02

(Connected to the uzh vpn from a non-uzh device. Necessary to connect to the Science Cluster.)

Opened `cmd.exe` on Windows 10.
```bash
ssh dwalth@cluster.s3it.uzh.ch
cd ~
srun --pty -n 1 -c 8 --time=01:00:00 --gres=gpu --mem=16G bash -l  # interactive gpu compute session
    # jobid: 667913, node: u20-computeibmgpu-vesta7 (A100)

module load anaconda3
source activate pytorch3dunet
```

To avoid booking 24 hours of A100 compute without computations (like yesterday), I do some checks before submission:
1. I first make sure that the given directories do exist and are the correct ones.
2. I next make sure that the `train3dunet` command actually starts running and producing some results.

```bash
# in the current train_config.yml:
# path to the checkpoint directory
    checkpoint_dir: /home/dwalth/data/wolny/checkpoints/checkpoints_230401/
# path to the training datasets
    file_paths:
      - /home/dwalth/scratch/wolny/data/sample_230331/sample_train_reduced/
# path to the val datasets
    file_paths:
      - /home/dwalth/scratch/wolny/data/sample_230331/sample_val_reduced
# save above info to the config.yml
# scp this config.yml to the cluster via Win10 cmd.exe `scp`
scp C:\Users\Dancer\Documents\cluster-uzh\ClusterWolny\CommandProtocols\slurm_230401\dw_train_config_230401.yml dwalth@cluster.s3it.uzh.ch:\home\dwalth\data\wolny\configs\config_230402\

tensorboard --logdir ~/data/wolny/checkpoints/checkpoints_230401/logs/
train3dunet --config ~/data/wolny/configs/config_230402/dw_train_config_230401.yml

# rewrite (shorten) the slurm job script. scp it to the cluster via cmd.exe:
scp C:\Users\Dancer\Documents\cluster-uzh\ClusterWolny\CommandProtocols\slurm_230401\pyto3dun-train.sh dwalth@cluster.s3it.uzh.ch:~\data\wolny\jobs\
```

```bash
sbatch data/wolny/jobs/pyto3dun-train.sh
    # Submitted batch job 668060
squeue -u dwalth
    # JOBID    USER    STATE        CPU MIN_ME         TIME END_TIME             NODELIST(REASON)
    # 668060   dwalth  RUNNING        4    16G         0:32 2023-04-03T18:54:07  u20-computeibmgpu-vesta7
    # 668024   dwalth  RUNNING        2  7780M        11:41 2023-04-02T19:42:58  u20-compute-m2
        # firefox tensorboard interactive session
```

----- scrap snippets
```bash
# automated key presses (does not work on cluster, not installed)
# https://manpages.ubuntu.com/manpages/trusty/en/man1/xdotool.1.html
xdotool key ctrl+C
```