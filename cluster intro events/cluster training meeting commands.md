cluster training meeting commands
- - -

ssh dwalth@cluster.s3it.uzh.ch
quota  # shows available memory, etc.

# scp <local stuff> <destination>
## be in your local directory where the file is that you want to transfer
scp training.tar dwalth@cluster.s3it.uzh.ch:/scratch/dwalth/

## rsinc more intelligent than scp
### transfering many files - e.g. more than 500 - scp struggles with numbering stuff
### rsinc is a fully sync. program, not just a copying program.

#### btw, truly massive data transfers (maybe 3D data?) - >= 10TB~
#### we have a special tool: globus - is even better than rsinc, because it uses better/advanced networking protocols

tar xvf training.tar  # extract the tar zip
tar tvf training.tar  # view it

bash hello.sh

```bash
dwalth@u20-login-3:~/scratch/training$ bash hello.sh
hello starting.
u20-login-3
Tue Feb 28 14:51:03 CET 2023
finished
```

- - -
# slurm
- - -

squeue  # JOB info.
squeue -A dwalth  # only displays 'dwalth's current running~ jobs.
	# I think you can also use `squeue -u dwalth`
sinfo  # NODE info. combine with squeue to find out about the currently available resources on the whole cluster.

- - -
# submitting a job from the login node
- - -
# double  ## marks comment lines in bash
# shebang ( `#bin/bash...`): specify language of your file.

sbatch hello.sh  # for actually submitting the jobs
  # sbatch jobscripts: use relative paths

- - - install stuff - - -

# virtual environments
module av  # probably lists available modules. confirmed
module load anaconda3
conda --help  # can use this since anaconda3 is loaded.
module list  # lists currently loaded modules
module purge # unloads currently loaded modules

# create new environment
module load anaconda3
conda create --name myenv python=3.10

# need larger virtual environment: NOT in login node!
# https://docs.s3it.uzh.ch/how-to_articles/how_to_run_an_interactive_session/
## just moves you to a compute node (from a login node)
srun --pty -n 1 -c 2 --time=01:00:00 --gres=gpu:1 --mem=8G bash -l
source activate myenv

#srun ...
# note: the flags: they are the same as in the sbatch commands / jobscript files

# on compute node / and/or in your virtual environment:
top, h top, screen, &, <interactive sessions>  # combination: useful for testing
cat conda.rc  # shows resources (?aha - maybe the usage depends on CLI usage vs. MS/Borland C~ comp. usage)











- - - - - nvm... trash...
- - - trash 1 - - -
dwalth@u20-login-3:~/scratch/training$ cat hello.sh
#!/bin/bash

### Comment lines start with ## or #+space
### Slurm option lines start with #SBATCH

### Here are the SBATCH parameters that you should always consider:
#SBATCH --time=0-00:05:00   ## days-hours:minutes:seconds
#SBATCH --mem 3000M         ## 3GB ram (hardware ratio is < 4GB/core)
#SBATCH --ntasks=1          ## Not strictly necessary because default is 1
#SBATCH --cpus-per-task=1   ## Use greater than 1 for parallelized jobs

### Here are other SBATCH parameters that you may benefit from using, currently commented out:
###SBATCH --job-name=hello1 ## job name
###SBATCH --output=job.out  ## standard out file


echo 'hello starting.'

hostname        ## Prints the system hostname

date            ## Prints the system date

echo 'finished'
- - -