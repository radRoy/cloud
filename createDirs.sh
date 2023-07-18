#dir=$1  # works
#dir='protocols'  # works
#dir=$(date)  # works
#dir=$(date '+chpt-%y%m%d-0')  # works

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
    mkdir "$dir"
    #echo "Created directory ${dir}"
    echo "~/data/outputs/${dateString}"
    break
  fi

done
