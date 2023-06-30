#dir=$1  # works
#dir='protocols'  # works
#dir=$(date)  # works
#dir=$(date '+chpt-%y%m%d-0')  # works

dirDate=$(date '+chpt-%y%m%d')  # works
i=0  # works
dir="${dirDate}-$i"  # works
#file $dir

while [ 1 ]
do
  dir="${dirDate}-$i"  # works
  # if [ directory <argument> exists]
  if [ -d "$dir" ]; then  # works
    echo $i  # exists
    ((i++))
    continue
  
  else  # if dir does not exist
    mkdir "$dir"
    break
  fi

done
