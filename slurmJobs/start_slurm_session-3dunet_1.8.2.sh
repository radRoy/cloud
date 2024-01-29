#!/bin/bash

source ~/(dirname $0)/../bash_scripts/prompt_yn.sh  # f_prompt_yn

# navigating directories and pulling newest committed files
cd /home/dwalth/data/cloud  # set working directory (only works on the ScienceCluster (uzh))
bash pull-script.sh  # in case that got forgotten

source ./bashScripts/getNextSession.sh
current_session=$(f_get_next_session)

output_root="/home/dwalth/data/outputs"

# creating the session string (makes it possible to give a custom session name as input, defaults to current date and a number yymmdd-id), e.g.: '230930-0'
if [ $# -eq 0 ]; then
    echo "Error. At least 1 input argument required (3dunet_type: 'train' or 'predict')."
    exit

else
    3dunet_type=$1
    if ! [ 3dunet_type == "train" || 3dunet_type == "predict" ]; then
        echo "Error. The 1st argument 3dunet_type must be either 'train' or 'predict'."
        exit
    fi

    if [ $# -gt 2 ]; then
        echo "Error. At most 2 input arguments expected (3dunet_type, input_session). More input arguments are not supported yet."
        exit
    
    elif [ $# -eq 2 ]; then
        input_session=$2
        echo "Input session provided: ${input_session}"
        if [ input_session == current_session ]; then
            echo "Error. The input session ID = current session ID (input ${input_session}, current ${current_session})."
            exit
        fi

        input_dir=$output_root/chpt-$input_session
        if ! [ -d input_dir ]; then
            echo "Error. Input directory '${input_dir}' does not exist."
            exit
        else
            echo "Input directory: ${input_dir}"
        fi
    
    else
        input_session="-"
        input_dir="-"
    fi
fi

if [ 3dunet_type == "train" ]; then
    # perform all the checks (does sbatch script exist? etc.)
    
    if [ input_session != "-" ]; then
        echo "Error. Continuing training with pre-trained weights is not supported yet by my bash scripts, sorry. I'm sure train3dunet can handle it if you do it manually, though."
        exit
    fi

    output_dir=$output_root/chpt-$current_session
    if [ -d output_dir ]; then
        if f_prompt_yn "Warning, the output directory ${output_dir} already exists. Continue? [y/n]"; then
            echo "Continuing with this ${3dunet_type}3dunet output directory."
        else
            echo "Error in ${3dunet_type}3dunet pipeline: output directory ${output_dir} already exists."
            exit
        fi
    else
        mkdir $output_dir
    fi

    # check if the slurm bash script exists
    3dunet_bash_script=./named_copies/slurm_job

    # check whether the config yaml exists
        
    slurm_out=$output_dir/slurm-$current_session.out  # file path to the slurm output file

    # run the train3dunet sbatch script
    sbatch --output=$slurmout

else  # 3dunet_type must be either 'train' or 'predict' as checked above
    # perform all the checks (does sbatch script exist? etc.)

    if [ input_session == "-" ]; then
        echo "Error. When running predict3dunet, the 'input_session' must be provided so this script can deduce where to take the pytorch checkpoint file from."
        exit
    fi
    
    output_dir=$input_dir/chpt-$current_session
    output_dir=$(get_output_dir())
    if [ -d output_dir ]; then
        if f_prompt_yn "Warning, the output directory ${output_dir} already exists. Continue? [y/n]"; then
            echo "Continuing with this ${3dunet_type}3dunet output directory."
        else
            echo "Error in ${3dunet_type}3dunet pipeline: output directory ${output_dir} already exists."
            exit
        fi
    else
        mkdir $output_dir
    fi

    # check if the slurm bash script exists

    # check whether the config yaml exists

    slurm_out=$output_dir/slurm-$current_session.out  # file path to the slurm output file

    # run the predict3dunet sbatch script
fi




















##############################################################
####################### old code below #######################
##############################################################




# creating the session's checkpoint directory if necessary
checkdir="/home/dwalth/data/outputs/chpt-${session}"
if ! [ -d "$checkdir" ]; then
    mkdir $checkdir
fi

###############################################################
# automated sbatch input argument handling would be done here #
###############################################################

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
