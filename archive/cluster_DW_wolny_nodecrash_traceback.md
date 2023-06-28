ssh dwalth@cluster.s3it.uzh.ch
 uzh AD password (/ ssh key etc.)

[wolny/pytorch-3dunet installation](https://github.com/wolny/pytorch-3dunet#installation)

```
ssh <shortname>@cluster.s3it.uzh.ch
cd scratch
module load anaconda3
/scratch$ conda create -n pytorch3dunet -c pytorch -c conda-forge -c awolny pytorch-3dunet
==> WARNING: A newer version of conda exists. <==   ok, nvm
  current version: 22.9.0
  latest version: 23.1.0
...
  environment location: /home/dwalth/data/conda/envs/pytorch3dunet
    # the "environment location" is on the cluster, ofc
following packages will be downloaded: <list>
following NEW packages will be installed: <list> # list contains pytorch 3d unet... (duh)
Proceed ([y]/n)? y
...
Preparing transaction: done
Verifying transaction: failed

CondaVerificationError: The package for keyutils located at /home/dwalth/data/conda/pkgs/keyutils-1.6.1-h166bdaf_0
appears to be corrupted. The path 'share/man/man7/asymmetric-key.7'
specified in the package manifest cannot be found.
```

```
~$ cd scratch  # still unsure about the thing written above (same command)...
~/scratch$ module load anaconda3
~/scratch/training$ conda create -n pytestenv
  environment location: /home/dwalth/data/conda/envs/pytestenv
~/scratch/training$ conda activate pytestenv
> CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.
To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell

See 'conda init --help' for more information and options.

IMPORTANT: You may need to close and restart your shell after running 'conda init'.
```
~/scratch/training$ srun --pty -n 1 -c 16 --time=01:00:00 --gres=gpu:A100:1 --mem=64G bash -l




## another try (this time not on the login node as I tried to before)

open cmd.exe in Windows 10.
```
ssh <shortname>@cluster.s3it.uzh.ch
cd scratch
```
idk, whether I have to go to the scratch dir before starting the interactive session on a compute node.  
**TBD**: Try this out (i.e., the other way around) in the next session.

**Starting** (running) an [interactive session](https://docs.s3it.uzh.ch/how-to_articles/how_to_run_an_interactive_session/):
```
~/scratch$ srun --pty -n 1 -c 2 --time=01:00:00 --gres=gpu:T4:1 --mem=7G bash -l
```

Now, the CLI/console... looks like this:
```
dwalth@u20-computegpu-4:/scratch/dwalth$ ls -la
total 4
drwx------   4 dwalth s3it_t_cluster_users    5 Mar 16 14:51 .
drwxr-xr-x 728 root   root                  727 Mar 16 13:49 ..
-rwxr-xr-x   1 dwalth dwalth                310 Feb  9 15:46 ._training
-rw-rw-r--   1 dwalth dwalth               1921 Feb 28 16:46 bash_history_cluster_train_session.txt
drwxrwxr-x   8 dwalth dwalth                 12 Mar 16 14:51 pytorch-3dunet
drwxr-xr-x   2 dwalth dwalth                  6 Feb 28 15:48 training
-rw-rw-r--   1 dwalth dwalth               1493 Feb 28 14:48 training.tar
```
Note that the pytorch-3dunet folder was git cloned there, onto my scratch drive, before I moved to (ran/started) the interactive session (...on a compute node, ofc).  
The `pwd` (present working directoy) prefix `/scratch/dwalth$` is omitted from here on.

Moving on to the conda environments for installing everything needed for the [wolny/pytorch-3dunet](https://github.com/wolny/pytorch-3dunet) to run:
```
module load anaconda3
conda create -n pytorch3dunet -c pytorch -c conda-forge -c awolny pytorch-3dunet
```
This produces this output:
```
NotWritableError: The current user does not have write permissions to a required path.
  path: /home/dwalth/.conda/envs/.conda_envs_dir_test
  uid: 891903425
  gid: 891903425

If you feel that permissions on this path are set incorrectly, you can manually
change them by executing

  $ sudo chown 891903425:891903425 /home/dwalth/.conda/envs/.conda_envs_dir_test

In general, it's not advisable to use 'sudo conda'.
```
At this stage, I am not comfortable enough with the science cluster to `sudo chown ...` (change permissions) anything in a `.<dirname>` (hidden) directory.  
Therefore, my approach is now to try other installation routes given by the (same) [wolny/pytorch-3dunet](https://github.com/wolny/pytorch-3dunet) repo.

Based on [conda create environment from yml / yaml file](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file ):  
**state of progress (node failure during command completion suggestion) - refer to section Appendix(\*1) in this document**
```
conda env create -f pytorch-3dunet/environment.yml
```
*"The first line of the yml file sets the new environment's name. For details see Creating an environment file manually.  
Activate the new environment: `conda activate myenv`"*  
This part should be done with `source activate <myenvname>`, as instructed by the science cluster team (refer to this [how-to: create env. on the cluster](https://docs.s3it.uzh.ch/how-to_articles/how_to_use_conda/#create-your-environment)):
```
source activate 3dunet
```
As written above, the name `3dunet` was taken from the pytorch-3dunet `environment.yaml` from their repo.

*"Verify that the new environment was installed correctly:"*
```conda env list``` 
*"You can also use conda `info --envs`."*


**Closing** the interactive session (manually, not by letting the time run out, if possible):
...Well, this did not work out as planned (refer to Appendix(\*1) for finding out why).

## Appendix (e.g., error reports)

Appendix(\*1), error - computegpu-4 node crashed:
```
dwalth@u20-computegpu-4:/scratch/dwalth$ conda env create -f srun: error: Node failure on u20-computegpu-4
srun: error: Node failure on u20-computegpu-4
srun: Force Terminated job 610938
dwalth@u20-login-2:~/scratch$
```
Where on the command's line, after the `conda env create -f ` I did this:  
- <press TAB for autocompletion;
- wait;
- press CTRL+C to cancel;
- realise I overloaded (somehow, probably the memory... idk) the node by searching all files for possible matches (which is something that `conda` does when you let it autocomplete this part (it first checks the system PATH, then other locations...). I can not find the webpage I have this information from (during the time of this interactive session));
- wait for node to crash;> :-(  
`srun: error: Node failure on u20-computegpu-4`
