#!/bin/bash

# navigating directories and pulling newest committed files
cd /home/dwalth/data/cloud
bash pull-script.sh  # in case that got forgotten

# creating the session string (makes it possible to give a custom session name as input, defaults to current date and a number yymmdd-id)
if ! [ $# -eq 0 ]; then
    session=$1
else
    source ./getNextSession.sh
    session=$(nextSession)
fi

# creating the session's checkpoint directory if necessary
checkdir="/home/dwalth/data/outputs/chpt-${session}"
if ! [ -d "$checkdir" ]; then
    mkdir $checkdir
fi

# calling the slurm job file (containing the train3dunet command, for example)
slurmout=slurm-$session.out
sbatch /home/dwalth/data/cloud/slurmJobs/named_copies/slurm_job-$session.sh $session $checkdir $slurmout

# copying outputs (should get executed after the slurm job has finished, for whatever reason)
backup_checkdir="/home/dwalth/data/backup_outputs/chpt-${session}"  # without trailing slash
if ! [ -d "$backup_checkdir" ]; then
    mkdir $backup_checkdir
fi
mv $slurmout $checkdir/
cp $checkdir/* $backup_checkdir/
