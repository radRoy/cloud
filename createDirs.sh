i = 0
dir = $(date '+chpt-%y%m%d-')
dirNum = dir + $i
echo dirNum

while [ $i -le 2 ]
do
  # if [ directory <argument> exists]
  if [ -d "$1" ]; then
    ((i++)); continue
  else
    
  fi
  
if [ dir-$i exists not ]; then
    ((i++))
    continue

  else
    echo $(date '+chpt-%y%m%d-' + $i)  # substitute echo with mkdir after testing
    break
  fi

  ((i++))

done
