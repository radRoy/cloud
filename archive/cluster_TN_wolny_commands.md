```
https://github.com/wolny/pytorch-3dunet

module load anaconda3
```
<conda created new in>
```
srun --pty -n 1 -c 16 --time=01:00:00 --gres=gpu:A100:1 --mem=64G bash -l
```
=> interactive session

```
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116python

python -c 'import torch;print(torch.backends.cudnn.version())'
python -c 'import torch;print(torch.__version__)'

$verify torch

git clone https://github.com/wolny/pytorch-3dunet
cd pytorch-3dunet
pip install -e .
```

...something like that, and then he (Thomas Naert) started getting error messages about hardware & driver incompatibilities and the like.
