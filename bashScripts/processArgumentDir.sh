#dir=$1  # works
#dir='protocols'  # works
#dir=$(date)  # works
#dir=$(date '+chpt-%y%m%d-0')  # works

dirDate=$(date '+chpt-%y%m%d')  # works
i=0  # works
dir="${dirDate}-$i"  # works
file $dir

if [ -d "$dir" ]; then  # works
  ((i++))
  echo $i
  continue
else
  mkdir "$dir"
  break
fi
