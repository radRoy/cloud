# protocol (commands and otherwise) of today

author: Daniel Walther
creation date: 2023.04.03

copying data from the cmd.exe to the cluster:
```bash
scp -r Y:\Users\DWalther\Unet\Unet-sample-data-wolny\* dwalth@cluster.s3it.uzh.ch:/home/dwalth/scratch/wolny/data/confocal_boundaries/
	# works like this
```

## the `tensorboard` command requesting user input problem:

### tried, does not work:

- https://slurm.schedmd.com/sbatch.html#OPT_error
	- maybe the user input prompt gets suppressed if it gets written to a file from the very start (although it's not an error message that requests user input...)
- https://slurm.schedmd.com/sbatch.html#OPT_input
	- can direct slurm to connect the standard input to some file, but how to give the key pressing user input without `xdotool` or similar things installed on the cluster?
- https://slurm.schedmd.com/sbatch.html#OPT_output
	- this also sounds like it could work, but the only thing to be changed here could be the filename given to sbatch for putting its standard output into
- https://slurm.schedmd.com/sbatch.html#OPT_quiet
	- -Q, --quiet: Suppress informational messages **from sbatch** such as Job ID. Only errors will still be displayed.

### potential solutions to the `tensorboard` command requesting user input:

I emailed wolny@github.com (email: wolny101@gmail.com), the creator of pytorch-3dunet, about this problem.

I emailed the s3it cluster helpdesk about it, for a solution from the cluster sbatch side.