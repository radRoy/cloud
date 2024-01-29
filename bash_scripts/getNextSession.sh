#!/bin/bash
# gets the current session id (yymmdd-x)

function f_get_next_session () {
  date=$(date '+%y%m%d')
  chpt_date="chpt-${date}"

  folder="../outputs/"
  i=0
  dateString="${chpt_date}-$i"

  while [ 1 ]
  do
    dateString="${chpt_date}-$i"
    dir="${folder}${dateString}"

    # if [ directory <argument> exists]
    if [ -d "$dir" ]; then  # checks if directory "$dir" exists
      ((i++))
      continue
    
    else  # if dir does not exist
      output="${date}-$i"
      break
    fi

  done

  echo $output
}