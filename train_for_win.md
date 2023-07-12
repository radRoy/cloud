# Training 3D U-Net (`train3dunet`) once, not in parallel, for achieving goals ASAP

```bash
ssh dwalth@login1.cluster.s3it.uzh.ch
# assume the changes to train config files, input data transfers are done.
# assume all config yml files are commited to cloud computing repo cloned on the cluster.
cd ~/data/cloud/
bash pull-script.sh
# repeat this command until all the necessary directories are created
bash createDirs.sh
    ...
    Created directory chpts/chpt-230712-5-asap/
    # some commands (the same one as above) and outputs left out for simplicity

tmux   # creates a new tmux window
tmux list-sessions
    # 0: 1 windows  # or something like that. one tmux session required for nesting screen sessions in this workflow here.
srun --pty -n 1 -c 8 --mem=32G --time=24:00:00 --gres=gpu:V100:1 --constraint=GPUMEM32GB bash -l  # jobid 4008984 (date: 230712)

# the separate tumx-nested screen sessions are necessary for the tensorboard log files to be specific to each train command.
screen -S 3dunet-5
module load tensorboard anaconda3
tensorboard --logdir ~/data/cloud/chpts/chpt-230712-5-asap/
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230712-5-asap/nvidia-smi.log &
ps  # verify the nvidia-smi command actually works and is running (= is listed in this command's output)
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230712-5-patience10,factor0.5,val100,log25.yml
<CTRL + A + D>  # detach from this screen session
screen -ls  # verify the session was not accidentally terminated (CTRL + D is the command for session termination)
# running successfully

<C-b + d>  # = ctrl (hold) + b, let go of both, then press d (DETACH from that tmux windows (=session))
tmux list-sessions  # verify that the session was not accidentally terminated

<CTRL + D>  # log out of the cluster session to test whether the tmux keeps running
exit  # exit the cmd session to test same thing
ssh ...  # log in again to test same thing
tmux attach -t 0  # attach to the tmux session 0
screen -r 3dunet-0  # attach to a running screen session with a running train3dunet process, for testing
# everything keeps successfully running.
```

The GPU usage statistics in the above tmux session - note that the GPU memory usage is as expected around 30'000 MiB, this also means that all 5 `train3dunet` processes are still running (and no reattachment into the screen sessions is necessary for double-checking that):
```bash
dwalth@u20-computeibmgpu-vesta8:~/data/cloud$ nvidia-smi
Wed Jul 12 11:29:58 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.125.06   Driver Version: 525.125.06   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  On   | 00000000:B2:00.0 Off |                    0 |
| N/A   51C    P0    76W / 300W |  30143MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A   1589901      C   ...ztn55cwzrrhstk/bin/python     6026MiB |
|    0   N/A  N/A   1591256      C   ...ztn55cwzrrhstk/bin/python     6026MiB |
|    0   N/A  N/A   1592734      C   ...ztn55cwzrrhstk/bin/python     6026MiB |
|    0   N/A  N/A   1593760      C   ...ztn55cwzrrhstk/bin/python     6026MiB |
|    0   N/A  N/A   1595244      C   ...ztn55cwzrrhstk/bin/python     6026MiB |
+-----------------------------------------------------------------------------+
```
train_config-230712-5-patience10,factor0.5,val100,log25.yml