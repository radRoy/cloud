#!/bin/bash

# navigating directories
cd /home/dwalth/data/cloud

# loading needed script file
source ./getNextSession.sh

# defining the number of sessions to be run (and prepared for) today (230930)
n=$((18))

# # getting today's date
# date=$(date '+%y%m%d')

# iteratively starting/submitting all prepared slurm jobs
while ((i < n)); do
    
    # getting the next session (the next to be created checkpoint output directory at ~/data/outputs/chpt-$session)
    session=$(nextSession)
    
    # creating the session's checkpoint directory if necessary
    checkdir="/home/dwalth/data/outputs/chpt-${session}"
    if ! [ -d "$checkdir" ]; then
        mkdir $checkdir
    fi
    
    echo "entering command: bash ./slurmJobs/start_slurm_session.sh $session"
    bash ./slurmJobs/start_slurm_session.sh $session
    ((i++))

done