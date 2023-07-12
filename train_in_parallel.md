# Training 3D U-Net (`train3dunet`) multiple times in parallel

## On the same node

### ... with `&`

I assume that, for all processes being run with a trailing `&`, the shell session attempts to run them simultaneously, i.e., as parallel threads of some sort. Therefore, for, e.g., 5 `train3dunet` commands to run in parallel on the same node, and each training process requiring, e.g., 6'050 MiB VRAM at its peak, the GPU on that node would require at least 30'250 MiB of VRAM.

The numbers above are taken from the 230710 run, i.e., from the babb03-ct3 data set, with specimens' images cropped individually and all scaled by 0.25, with a patch shape of 80, 160, 160, and a stride shape of 20, 40, 40.

The separate tumx-nested screen sessions are necessary for the tensorboard log files to be specific to each train command. The separate `train3dunet` could also be run in the same ssession with a trailing `&`, but that is not necessary, in the end, given the separating screen sessions working just fine inside tmux sessions.

The commands I plan to enter in the shell are the following:

```bash
ssh dwalth@login1.cluster.s3it.uzh.ch
# assume the changes to train config files, input data transfers are done.
cd ~/data/cloud/
bash pull-script.sh

tmux   # creates a new tmux window
tmux list-sessions
    0: 1 windows  # or something like that. one tmux session required for nesting screen sessions in this workflow here.
srun --pty -n 1 -c 8 --mem=32G --time=24:00:00 --gres=gpu:V100:1 --constraint=GPUMEM32GB bash -l  # jobid 4008984 (date: 230712)

# the separate tumx-nested screen sessions are necessary for the tensorboard log files to be specific to each train command.
screen -S 3dunet-0
module load tensorboard anaconda3
tensorboard --logdir ~/data/cloud/chpts/chpt-230712-0/
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230712-0/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230712-0/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230712-0-patience10,factor0.25.yml
<CTRL + A + D>  # detach from this screen session
screen -ls  # verify the session was not accidentally terminated (CTRL + D is the command for session termination)

screen -S 3dunet-1
module load tensorboard anaconda3
tensorboard --logdir ~/data/cloud/chpts/chpt-230712-1/
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230712-1/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230712-1/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230712-1-patience10,factor0.3.yml
<CTRL + A + D>  # detach from this screen session
screen -ls  # verify the session was not accidentally terminated (CTRL + D is the command for session termination)

screen -S 3dunet-2
module load tensorboard anaconda3
tensorboard --logdir ~/data/cloud/chpts/chpt-230712-2/
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230712-2/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230712-2/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230712-2-patience10,factor0.35.yml
<CTRL + A + D>  # detach from this screen session
screen -ls  # verify the session was not accidentally terminated (CTRL + D is the command for session termination)

screen -S 3dunet-3
module load tensorboard anaconda3
tensorboard --logdir ~/data/cloud/chpts/chpt-230712-3/
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230712-3/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230712-3/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230712-3-patience10,factor0.4.yml
<CTRL + A + D>  # detach from this screen session
screen -ls  # verify the session was not accidentally terminated (CTRL + D is the command for session termination)

screen -S 3dunet-4
module load tensorboard anaconda3
tensorboard --logdir ~/data/cloud/chpts/chpt-230712-4/
source activate 3dunet
nvidia-smi -i $CUDA_VISIBLE_DEVICES -l 2 --query-gpu=gpu_name,memory.used,memory.free --format=csv -f ~/data/cloud/chpts/chpt-230712-4/nvidia-smi.log &
tensorboard --logdir /home/dwalth/data/cloud/chpts/chpt-230712-4/
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230712-4-patience10,factor0.45.yml
<CTRL + A + D>  # detach from this screen session
screen -ls  # verify the session was not accidentally terminated (CTRL + D is the command for session termination)

<C-b + d>  # = ctrl (hold) + b, let go of both, then press d (DETACH from that tmux windows (=session))
```
