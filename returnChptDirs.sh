#!/bin/bash
# creates an empty directory at a pre-determined location somewhere on the Science Cluster

function checkpoint {
  date=$(date '+chpt-%y%m%d')  # works

  prefix="../outputs/"
  i=0  # works
  dateString="${date}-$i"  # works

  while [ 1 ]
  do
    dateString="${date}-$i"  # works
    dir="${prefix}${dateString}"
    # if [ directory <argument> exists]
    if [ -d "$dir" ]; then  # works (checks if directory "$dir" exists)
      #echo $i  # exists
      ((i++))
      continue
    
    else  # if dir does not exist
      #mkdir "$dir"
      #echo "Created directory ${dir}"
      output="~/data/outputs/${dateString}"
      break
    fi

  done

  return output
}