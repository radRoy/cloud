if [ -d "$1" ]; then
  file $1
  echo "$1 should exist"
else
  file $1
  echo "$1 should not exist"
fi
