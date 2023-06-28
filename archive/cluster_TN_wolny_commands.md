# Installation of the pytorch-3dunet repository

[Installation notes](https://github.com/wolny/pytorch-3dunet)

```bash
ssh <shortname>@login1.cluster.s3it.uzh.ch
module load anaconda3
conda create -n 3dunet
source active 3dunet

(3dunet) conda install pip
(3dunet) pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116python
(3dunet) python -c 'import torch;print(torch.backends.cudnn.version())'
    #8500
(3dunet) python -c 'import torch;print(torch.__version__)'
    #2.0.1+cu117
#(3dunet) $verify torch  # command  'torch' unknown


#<navigate to the cloned repo of interest (to have environment.yml ready, etc.)>
```

Under wolny's installation tips, it says that checking the compatibility with installed CUDA versions, etc. is recommended. Therefore:  
Starting an interactive session with the hardware that is to be used when training models:  
```bash
srun --pty -n 1 -c 16 --time=01:00:00 --gres=gpu:A100:1 --mem=64G bash -l
```

```bash
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116python

python -c 'import torch;print(torch.backends.cudnn.version())'
python -c 'import torch;print(torch.__version__)'

$verify torch

git clone https://github.com/wolny/pytorch-3dunet
cd pytorch-3dunet
pip install -e .
```

...something like that, and then he (Thomas Naert) started getting error messages about hardware & driver incompatibilities and the like.
