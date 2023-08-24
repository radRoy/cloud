"""
Daniel Walther
creation date: 23.08.2023 (dd.mm.yyyy)
purpose: Handling the yaml files involved in training a 3dunet model on the UZH's Science Cluster (and maybe a little more or less).
"""

import yaml
import datetime
import copy

# today's date string in yymmdd format
today_date = datetime.date.today()  # today's date in yyyy-mm-dd format, <class 'datetime.date'>
today = str(today_date)[2:].replace('-', '')  # mutate yyyy-mm-dd date string to yymmdd, e.g. 230823

config_testing_yaml = 'pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config_testing.yml'
config_yaml = 'pytorch-3dunet/resources/DW-3DUnet_lightsheet_boundary/train_config.yml'

with open(config_testing_yaml, 'r') as train_config:

    # relevant values (hyper parameters) that I changed or checked at some point in my MSc thesis project
    yaml_dict = yaml.safe_load(train_config)
    input_lines_dict = {
        'in_channels': [8, yaml_dict['model']['in_channels']],
        'out_channels': [10, yaml_dict['model']['out_channels']],
        'factor': [45, yaml_dict['lr_scheduler']['factor']],
        'patience': [46, yaml_dict['lr_scheduler']['patience']],
        'checkpoint_dir': [51, yaml_dict['trainer']['checkpoint_dir']],
        'validate_after_iters': [58, yaml_dict['trainer']['validate_after_iters']],
        'log_after_iters': [60, yaml_dict['trainer']['log_after_iters']],
        'max_num_epochs': [62, yaml_dict['trainer']['max_num_epochs']],
        'max_num_iterations': [64, yaml_dict['trainer']['max_num_iterations']],
        'raw_internal_path': [70, yaml_dict['loaders']['raw_internal_path']],
        'label_internal_path': [72, yaml_dict['loaders']['label_internal_path']],
        'train_file_paths': [77, yaml_dict['loaders']['train']['file_paths']],
        'train_patch_shape': [85, yaml_dict['loaders']['train']['slice_builder']['patch_shape']],
        'train_stride_shape': [87, yaml_dict['loaders']['train']['slice_builder']['stride_shape']],
        'val_file_paths': [133, yaml_dict['loaders']['val']['file_paths']],
        'val_patch_shape': [139, yaml_dict['loaders']['val']['slice_builder']['patch_shape']],
        'val_stride_shape': [141, yaml_dict['loaders']['val']['slice_builder']['stride_shape']]
    }

    # Output lines' dictionary's data format: {hyper_parameter: [line_index_of_value, value]},
    # where "line_index_of_value" starts at 0 for the first line,
    # and marks the line containing a hyper parameter's value.
    output_lines_dict = copy.deepcopy(input_lines_dict)

    # list of the line numbers with hyper parameter values to be replaced
    parameter_names = [key for key in input_lines_dict.keys()]
    line_numbers = [value[0] for value in input_lines_dict.values()]
    input_parameter_values = [value[1] for value in input_lines_dict.values()]

    # TBD: change the values of desired hyper parameters
    #output_lines_dict = ...
    latest_checkpoint_dir = output_lines_dict['checkpoint_dir'][1]
    if today in latest_checkpoint_dir:
        print(f' A session from today found in config yaml.')
        session_id = int(
            latest_checkpoint_dir.split('-')[-1].strip('/'))  # extract and convert to int the trailing session id
        # print(f'session id: {session_id}')
        new_checkpoint_dir = f'/home/dwalth/data/outputs/chpt-{today}-{session_id + 1}/'
    else:
        print(f' No session from today found in config yaml.')
        new_checkpoint_dir = f'/home/dwalth/data/outputs/chpt-{today}-0/'
    print(f'new checkpoint dir: {new_checkpoint_dir}')
    output_lines_dict['checkpoint_dir'][1] = new_checkpoint_dir

    # test for inputdict different than outputdict
    print(input_lines_dict['checkpoint_dir'][1])
    print(output_lines_dict['checkpoint_dir'][1])

    # list of the output parameter values containing the changed values
    output_parameter_values = [value[1] for value in output_lines_dict.values()]

# opening the same yaml file again for creating the replacement lines (maybe then readlines() is not empty again)
with open(config_testing_yaml, 'r') as train_config:
    # going through the yaml file, replacing input with output values in new variable, line by line
    new_yaml = ''
    lines = train_config.readlines()
    for i, line in enumerate(lines):
        #print('line:', line)
        if i in line_numbers:
            new_line = line.replace(
                str(input_parameter_values[line_numbers.index(i)]),
                str(output_parameter_values[line_numbers.index(i)])
            )
        else:
            new_line = line
        #new_yaml.append(new_line)
        new_yaml += new_line
    #print(f'yaml:\n{new_yaml}')
#print(f'yaml:\n{new_yaml}')

# write the output, updated, yaml to file
with open(config_testing_yaml, 'w') as new_train_config:
    new_train_config.write(new_yaml)
