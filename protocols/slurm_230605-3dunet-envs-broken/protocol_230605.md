daniel walther
creation date: 05.06.2023

```bash
module load anaconda3
source activate envWolny
# or:
#source activate pytorch3dunet, should be identical
srun --pty -n 1 -c 8 --gres=gpu:V100:1 --constraint=GPUMEM32GB --mem=64G --time=01:00:00 bash -l
train3dunet ...
```

The conda environments `envWolny` and `pytorch3dunet` both worked, previously, and now they do not recognise the command `train3dunet` anymore. Unclear, why.
I will just delete these folders and reinstall the repo's conda environment.