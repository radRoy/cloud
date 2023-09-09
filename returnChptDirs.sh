#!/bin/bash
# returns the next would-be created directory by cloud/createChptDirs.sh

function f_returnCheckpoint {
  date=$(date '+chpt-%y%m%d')

  path="/home/dwalth/data/outputs"
  i=0
  dateString="${date}-$i"

  while [ 1 ]
  do
    dateString="${date}-$i"
    dir="${path}/${dateString}"
    # if [ directory <argument> exists]
    if [ -d "$dir" ]; then  # checks if directory "$dir" exists
      ((i++))
      continue
    
    else  # if dir does not exist
      output=$dir
      break
    fi

  done

  echo $output  # absolute folder path starting with "/home/dwalth/..." without trailing slash
}