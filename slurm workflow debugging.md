# slurm workflow debugging
Daniel Walther
creation date: 30.05.2023

## `tensorboard --logdir` requires user input prompt

Email exchange with S3IT's Petra:

Last email from Petra:
>To wrap it up, have you tried to maybe NOT specify logdir initially, and instead at the end of your script move whatever data was created into a folder of your liking? Something like this:  
>  
>```bash  
>module load anaconda3  
>source activate pytorch3dunet
>    # alternatively use envWolny, should be identical, but built via different routes described on github.com/wolny/pytorch-3dunet  
>#tensorboard --logdir ~/data/wolny/checkpoints/checkpoints_230401/logs/  # trying to mute this output.  
>train3dunet --config ~/data/wolny/configs/config_230402/dw_train_config_230401.yml  
>
>mv runs/CURRENT_DATETIME_HOSTNAME ~/data/wolny/checkpoints/checkpoints_230401/logs/
>   #runs/CURRENT_DATETIME_HOSTNAME --> this seems to be default output  
>```  
>  

## 