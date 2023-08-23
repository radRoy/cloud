"""
Daniel Walther
creation date: 23.08.2023 (dd.mm.yyyy)
purpose: Handling the yaml files involved in training a 3dunet model on the UZH's Science Cluster (and maybe a little more or less).
"""

import yaml
import generateCheckpointDir
import datetime

# today's date string in yymmdd format
today_date = datetime.date.today()  # today's date in yyyy-mm-dd format, <class 'datetime.date'>
today = str(today_date)[2:].replace('-', '')  # mutate yyyy-mm-dd date string to yymmdd, e.g. 230823

config_testing_yaml = 'pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config_testing.yml'
config_yaml = 'pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml'
with open(config_testing_yaml, 'r') as train_config:
    print(f'\ntrain config testing yaml opened.\n')
    d_config = yaml.safe_load(stream=train_config)  # a dictionary of dictionaries (from parsing the given yml file)
    latest_checkpoint_dir = d_config['trainer']['checkpoint_dir']

    #today = not_today = '220823'
    print(today)
    print(latest_checkpoint_dir)
    if today in latest_checkpoint_dir:
        print(f'A session from today found in config yaml.')

        chpt_folders = latest_checkpoint_dir.split('/')
        chpt_folder = [part for part in chpt_folders if today in part][0]
        print(f'chpt_folder: {chpt_folder}')

        session_id = int(chpt_folder.split('-')[-1])
        print(f'session_id: {session_id}, type: {type(session_id)}')

        new_chpt_folder = f'chpt-{today}-{session_id + 1}'
        print(f'new_checkpoint_dir: {new_chpt_folder}')

        d_config['trainer']['checkpoint_dir'] = d_config['trainer']['checkpoint_dir'].replace(chpt_folder, new_chpt_folder)
        print(f"new checkpoint dir in dictionary: {d_config['trainer']['checkpoint_dir']}")

    else:
        print(f'No session from today found in config yaml.')
        # TBD: Do the other case
