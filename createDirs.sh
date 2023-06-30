i=0

while [ $i -le 2 ]
do

  if [ dir-$i exists not ]; then
    ((i++))
    continue

  else
    echo $(date '+chpt-%y%m%d-' + $i)  # substitute echo with mkdir after testing
    break
  fi

  ((i++))

done
