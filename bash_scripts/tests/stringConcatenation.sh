i=0
echo $i

dir=$(date)
echo $dir

dir+=$dir
echo $dir

concat="${dir}, ${i}"
echo $concat
