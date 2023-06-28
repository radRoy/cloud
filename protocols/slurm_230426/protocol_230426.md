# protocol (commands and otherwise) of today

author: Daniel Walther
creation date: 2023.04.26

copying data from the cmd.exe to the cluster:
	- use the globus.org service in the future
	- use rsync for command line transfer use cases in the future

## the `tensorboard` command requesting user input problem:

just run an interactive slurm session with the compute requirements of my otherwise sbatch job request.
first sort out changed file paths (adapt to today).  
(=>***TBD***)

Below is what was actually done today.

in my WSL ubuntu 20 (template from <https://docs.s3it.uzh.ch/cluster/data/>) home dir:
```bash
#rsync -az --progress my/local/dir <shortname>@cluster.s3it.uzh.ch:scratch/target
rsync -az --progress rsyncTest dwalth@cluster.s3it.uzh.ch:scratch/
	# sending incremental file list
	# rsyncTest/
	# rsyncTest/testfile.txt
	#              17 100%    0.00kB/s    0:00:00 (xfr#1, to-chk=0/2)
rsync -az --progress h5-488Int50raw-638Int50label  dwalth@cluster.s3it.uzh.ch:scratch/wolny/data/babb2.1/
	# sending incremental file list
	# h5-488Int50raw-638Int50label/
	# h5-488Int50raw-638Int50label/babb2.1-a5-01-otsuLabelled.h5
	#   1,447,257,571 100%   12.02MB/s    0:01:54 (xfr#1, to-chk=5/7)
	# h5-488Int50raw-638Int50label/babb2.1-a5-02-otsuLabelled.h5
	#   1,486,797,820 100%   11.84MB/s    0:01:59 (xfr#2, to-chk=4/7)
	# h5-488Int50raw-638Int50label/babb2.1-a5-03-otsuLabelled.h5
	#   1,563,517,566 100%   11.88MB/s    0:02:05 (xfr#3, to-chk=3/7)
	# h5-488Int50raw-638Int50label/babb2.1-a5-04-otsuLabelled.h5
	#   1,268,476,334 100%   11.82MB/s    0:01:42 (xfr#4, to-chk=2/7)
	# h5-488Int50raw-638Int50label/babb2.1-a5-05-otsuLabelled.h5
	#      42,401,792   3%    9.44MB/s    0:02:10
	# 	... <meanwhile (see following bash section)>
```
meanwhile wanting to cancel the so far unused interactive session:
```bash
# around We., 23:20~
# can not interactive in the interactive session window anymore...
# close that cmd window
# reopen cmd.exe and type:
C:\Users\Dancer>ssh dwalth@cluster.s3it.uzh.ch
	# dwalth@cluster.s3it.uzh.ch: Permission denied (publickey,hostbased).
# wtf, that's not nice ("hostbased", thanks a lot). probably idle for too long... but weird nonetheless.
```

```bash
#srun --pty -n 1 -c 4 --gres=gpu:A100 --mem=16G --time=27:00:00 bash -l
srun --pty -n 1 -c 4 --gres=gpu --mem=32G --time=24:00:00 bash -l
	# srun: job 843983 queued and waiting for resources
	# srun: job 843983 has been allocated resources
		# (1 min wait, again. nice (We., 20:36))

module load anaconda3; source activate envWolny; tensorboard --logdir /home/dwalth/data/wolny/checkpoints/checkpoints_230404/
```