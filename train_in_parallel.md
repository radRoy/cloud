# Training 3D U-Net (`train3dunet`) multiple times in parallel

## On the same node

### ... with `&`

I assume that, for all processes being run with a trailing `&`, the shell session attempts to run them simultaneously, i.e., as parallel threads of some sort. Therefore, for, e.g., 5 `train3dunet` commands to run in parallel on the same node, and each training process requiring, e.g., 6'050 MiB VRAM at its peak, the GPU on that node would require at least 30'250 MiB of VRAM.

The numbers above are taken from the 230710 run, i.e., from the babb03-ct3 data set, with specimens' images cropped individually and all scaled by 0.25, with a patch shape of 80, 160, 160, and a stride shape of 20, 40, 40.

The commands I plan to enter in the shell are the following:

```bash
ssh dwalth@login1.cluster.s3it.uzh.ch
# between these commands, terminate the process where the learning rate does not seem to decrease
screen -S
srun --pty -n 1 -c 8 --mem=32G --time=24:00:00 --gres=gpu:V100:1 --constraint=GPUMEM32GB bash -l
nvidia-smi ...
module load anaconda3 tensorboard
```
