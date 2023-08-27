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

## Final model output

```bash
train3dunet --config ~/data/cloud/pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/named_copies/train_config-230712-5-patience10,factor0.5,val100,log25.yml
    ...
    2023-07-12 18:18:32,387 [MainThread] INFO UNetTrainer - Training iteration [8875/150000]. Epoch [306/4999]
    2023-07-12 18:18:33,808 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:18:33,809 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:18:33,809 [MainThread] INFO UNetTrainer - Training stats. Loss: 1.0000003576278687. Evaluation score: 0.0
    2023-07-12 18:18:33,864 [MainThread] INFO UNetTrainer - Training iteration [8876/150000]. Epoch [306/4999]
    2023-07-12 18:18:42,418 [MainThread] INFO UNetTrainer - Training iteration [8877/150000]. Epoch [306/4999]
    2023-07-12 18:18:42,885 [MainThread] INFO UNetTrainer - Training iteration [8878/150000]. Epoch [306/4999]
    2023-07-12 18:18:44,279 [MainThread] INFO UNetTrainer - Training iteration [8879/150000]. Epoch [306/4999]
    2023-07-12 18:18:45,673 [MainThread] INFO UNetTrainer - Training iteration [8880/150000]. Epoch [306/4999]
    2023-07-12 18:18:47,068 [MainThread] INFO UNetTrainer - Training iteration [8881/150000]. Epoch [306/4999]
    2023-07-12 18:18:48,463 [MainThread] INFO UNetTrainer - Training iteration [8882/150000]. Epoch [306/4999]
    2023-07-12 18:18:49,861 [MainThread] INFO UNetTrainer - Training iteration [8883/150000]. Epoch [306/4999]
    2023-07-12 18:18:51,256 [MainThread] INFO UNetTrainer - Training iteration [8884/150000]. Epoch [306/4999]
    2023-07-12 18:18:52,657 [MainThread] INFO UNetTrainer - Training iteration [8885/150000]. Epoch [306/4999]
    2023-07-12 18:18:54,058 [MainThread] INFO UNetTrainer - Training iteration [8886/150000]. Epoch [306/4999]
    2023-07-12 18:18:55,458 [MainThread] INFO UNetTrainer - Training iteration [8887/150000]. Epoch [306/4999]
    2023-07-12 18:18:56,857 [MainThread] INFO UNetTrainer - Training iteration [8888/150000]. Epoch [306/4999]
    2023-07-12 18:18:58,270 [MainThread] INFO UNetTrainer - Training iteration [8889/150000]. Epoch [306/4999]
    2023-07-12 18:18:59,666 [MainThread] INFO UNetTrainer - Training iteration [8890/150000]. Epoch [306/4999]
    2023-07-12 18:19:01,071 [MainThread] INFO UNetTrainer - Training iteration [8891/150000]. Epoch [306/4999]
    2023-07-12 18:19:02,487 [MainThread] INFO UNetTrainer - Training iteration [8892/150000]. Epoch [306/4999]
    2023-07-12 18:19:03,902 [MainThread] INFO UNetTrainer - Training iteration [8893/150000]. Epoch [306/4999]
    2023-07-12 18:19:05,300 [MainThread] INFO UNetTrainer - Training iteration [8894/150000]. Epoch [306/4999]
    2023-07-12 18:19:06,713 [MainThread] INFO UNetTrainer - Training iteration [8895/150000]. Epoch [306/4999]
    2023-07-12 18:19:08,115 [MainThread] INFO UNetTrainer - Training iteration [8896/150000]. Epoch [306/4999]
    2023-07-12 18:19:09,530 [MainThread] INFO UNetTrainer - Training iteration [8897/150000]. Epoch [306/4999]
    2023-07-12 18:19:10,948 [MainThread] INFO UNetTrainer - Training iteration [8898/150000]. Epoch [306/4999]
    2023-07-12 18:19:12,365 [MainThread] INFO UNetTrainer - Training iteration [8899/150000]. Epoch [306/4999]
    2023-07-12 18:19:13,783 [MainThread] INFO UNetTrainer - Training iteration [8900/150000]. Epoch [306/4999]
    2023-07-12 18:19:15,203 [MainThread] INFO UNetTrainer - Validating...
    2023-07-12 18:19:15,999 [MainThread] INFO UNetTrainer - Validation iteration 0
    2023-07-12 18:19:16,654 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:16,654 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:16,655 [MainThread] INFO UNetTrainer - Validation iteration 1
    2023-07-12 18:19:17,041 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:17,042 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:17,042 [MainThread] INFO UNetTrainer - Validation iteration 2
    2023-07-12 18:19:17,441 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:17,441 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:17,442 [MainThread] INFO UNetTrainer - Validation iteration 3
    2023-07-12 18:19:17,850 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:17,850 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:17,851 [MainThread] INFO UNetTrainer - Validation iteration 4
    2023-07-12 18:19:18,248 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:18,248 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:18,248 [MainThread] INFO UNetTrainer - Validation iteration 5
    2023-07-12 18:19:18,649 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:18,649 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:18,649 [MainThread] INFO UNetTrainer - Validation iteration 6
    2023-07-12 18:19:19,046 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:19,046 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:19,046 [MainThread] INFO UNetTrainer - Validation iteration 7
    2023-07-12 18:19:19,443 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:19,443 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:19,443 [MainThread] INFO UNetTrainer - Validation iteration 8
    2023-07-12 18:19:19,841 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:19,841 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:19,841 [MainThread] INFO UNetTrainer - Validation iteration 9
    2023-07-12 18:19:20,244 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:20,244 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:20,245 [MainThread] INFO UNetTrainer - Validation iteration 10
    2023-07-12 18:19:20,643 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:20,644 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:20,644 [MainThread] INFO UNetTrainer - Validation iteration 11
    2023-07-12 18:19:21,048 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:21,048 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:21,048 [MainThread] INFO UNetTrainer - Validation iteration 12
    2023-07-12 18:19:21,454 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:21,454 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:21,454 [MainThread] INFO UNetTrainer - Validation iteration 13
    2023-07-12 18:19:22,569 [MainThread] INFO EvalMetric - ARand: 0.05864064884303932
    2023-07-12 18:19:22,570 [MainThread] INFO UNetTrainer - Validation iteration 14
    2023-07-12 18:19:22,961 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:22,961 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:23,142 [MainThread] INFO UNetTrainer - Validation finished. Loss: 1.6892108599344888. Evaluation score: 0.003909376589535955
    2023-07-12 18:19:23,144 [MainThread] INFO UNetTrainer - Saving checkpoint to '/home/dwalth/data/cloud/chpts/chpt-230712-5/last_checkpoint.pytorch'
    2023-07-12 18:19:23,594 [MainThread] INFO EvalMetric - Skipping ARandError computation: only 1 label present in the ground truth
    2023-07-12 18:19:23,595 [MainThread] INFO EvalMetric - ARand: 0.0
    2023-07-12 18:19:23,595 [MainThread] INFO UNetTrainer - Training stats. Loss: 0.8090771384796915. Evaluation score: 0.0
    2023-07-12 18:19:23,650 [MainThread] INFO UNetTrainer - Learning rate below the minimum 1e-06.
    2023-07-12 18:19:23,820 [MainThread] INFO UNetTrainer - Stopping criterion is satisfied. Finishing training
```