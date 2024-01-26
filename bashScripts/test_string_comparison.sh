#!/bin/bash

if [ $# -ne 0 ]; then
	echo "Input: $1"
	if [ $1 == "240126-0" ]; then
		echo "Input is equal to 240126-0. Bash string comparisons can be done with '-eq'."
	else
		echo "Input is not equal to 240126-0or string comparisons can not be done with '-eq'."
	fi
else
	echo "no input argument."
fi
