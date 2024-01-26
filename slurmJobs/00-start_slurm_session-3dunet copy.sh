#!/bin/bash

cd /home/dwalth/data/cloud  # navigating directories
bash pull-script.sh  # pulling newest committed files in case that got forgotten

# Taking the session string input argument, if there is an argument at all. e.g.: '240124-0'
if ! [ $# -eq 0 ]; then
    session_argument=$1
else
    session_argument=""
fi

# Creating the (current) session string (makes it possible to give a custom session name as input, defaults to current date and a number yymmdd-id). e.g.: '230930-0'
source ./getNextSession.sh
current_session=$(nextSession)

# Case where no input argument or the next session's ID (= 'current_session') is provided
if [ session_argument == "" -o session_argument == current_session ]
    checkpoint_dir="/home/dwalth/data/outputs/chpt-${current_session}"
    if ! [ -d "$checkpoint_dir" ]; then
        mkdir $checkpoint_dir  # creating the session's checkpoint directory if necessary
    fi
    output_dir="/home/dwalth/data/outputs/chpt-${current_session}"

    # calling the slurm job file (containing the train3dunet command, for example)
    slurmout=$checkpoint_dir/slurm-$current_session.out
    if [ -f $slurmout ]; then
        i=0
        while [ -f slurmout ]
        do
            slurmout=$checkpoint_dir/slurm-$current_session-$i.out
            ((i++))
        done
    fi
    
    slurm_script="/home/dwalth/data/cloud/slurmJobs/named_copies/slurm_job-${current_session}.sh"
    if [ -f $slurm_script ]; then
        sbatch --output=$slurmout $slurm_script $session $checkpoint_dir $slurmout
        sbatch --output=$slurmout $slurm_script $session_argument $current_session $checkpoint_dir $output_dir $slurmout
    else
        echo "Error: Slurm script: ${slurm_script} could not be found."
    fi

else  # handling input argument

    checkpoint_dir="/home/dwalth/data/outputs/chpt-${session_argument}"
    if [ -d $checkpoint_dir ]; then  # code when input dir valid (exists already)
    
        slurm_script="/home/dwalth/data/cloud/slurmJobs/named_copies/slurm_job-${current_session}.sh"
        if [ -f $slurm_script ]; then
            output_dir="/home/dwalth/data/outputs/chpt-${session_argument}/chpt-${current_session}"
            sbatch --output=$slurmout $slurm_script $session_argument $current_session $checkpoint_dir $output_dir $slurmout
        else
            echo "Error: Slurm script: ${slurm_script} could not be found."
        fi
    
    else  # code when input dir invalid (does not exist)
        echo "Error: The provided input for the session argument: ${session_argument} is invalid."
    fi
fi

# copying outputs (should get executed after the slurm job has finished, for whatever reason)
### This does not work, currently. Need to find a way to wait for above 'sbatch' process to finish before executing these lines.
## backup_checkdir="/home/dwalth/data/backup_outputs/chpt-${session}"  # without trailing slash
## if ! [ -d "$backup_checkdir" ]; then
##     mkdir $backup_checkdir
## fi
## mv $slurmout $checkdir/
## cp $checkdir/* $backup_checkdir/
