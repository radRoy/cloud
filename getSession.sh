#!/bin/bash
# gets the current session id (yymmdd-x)

function session {
  date=$(date '+chpt-%y%m%d')

  prefix="../outputs/"
  i=0
  dateString="${date}-$i"

  while [ 1 ]
  do
    dateString="${date}-$i"
    dir="${prefix}${dateString}"
    # if [ directory <argument> exists]
    if [ -d "$dir" ]; then  # checks if directory "$dir" exists
      ((i++))
      continue
    
    else  # if dir does not exist
      output="${dateString}"
      break
    fi

  done

  echo $output
}