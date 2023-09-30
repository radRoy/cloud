#!/bin/bash

# navigating directories
cd /home/dwalth/data/cloud

# loading needed script file
source ./getNextSession.sh

# defining the number of sessions to be run (and prepared for) today (230930)
n=18

# getting today's date
date=$(date '+%y%m%d')

# iteratively starting/submitting all prepared slurm jobs
while (( $i < $n )); do
    
    session="${date}-${i}"
    echo "i: ${i}, session: ${session}"
    echo " bash slurmJobs/start_slurm_session.sh $session"

    ((i++))
done