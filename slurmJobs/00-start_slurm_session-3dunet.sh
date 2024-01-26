#!/bin/bash

# navigating directories and pulling newest committed files
cd /home/dwalth/data/cloud
# bash pull-script.sh  # in case that got forgotten

# taking the session string input argument, if there is an argument at all. e.g.: '240124-0'
if ! [ $# -eq 0 ]; then
    session_argument=$1
else
    session_argument=""
fi

# creating the (current) session string (makes it possible to give a custom session name as input, defaults to current date and a number yymmdd-id)
# session example: '230930-0'
source ./getNextSession.sh
session=$(nextSession)

if [session_argument -eq "" -o]
    # creating the session's checkpoint directory if necessary
    checkdir="/home/dwalth/data/outputs/chpt-${session}"
    if ! [ -d "$checkdir" ]; then
        mkdir $checkdir
    fi

    # calling the slurm job file (containing the train3dunet command, for example)
    slurmout=$checkdir/slurm-$session.out
    sbatch --output=$slurmout /home/dwalth/data/cloud/slurmJobs/named_copies/slurm_job-$session.sh $session $checkdir $slurmout

# copying outputs (should get executed after the slurm job has finished, for whatever reason)
### This does not work, currently. Need to find a way to wait for above 'sbatch' process to finish before executing these lines.
## backup_checkdir="/home/dwalth/data/backup_outputs/chpt-${session}"  # without trailing slash
## if ! [ -d "$backup_checkdir" ]; then
##     mkdir $backup_checkdir
## fi
## mv $slurmout $checkdir/
## cp $checkdir/* $backup_checkdir/
