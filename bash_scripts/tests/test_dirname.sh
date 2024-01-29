#!/bin/bash

cd ~
mkdir super_dir_empty
cd ~/super_dir_empty

echo "pwd $(pwd)"
echo $(dirname $0)  # returns path in ~/path/$0
cd ~/$(dirname $0)  # changes directory to this script's parent
echo "pwd $(pwd)"

cd ~
rm -d super_dir_empty