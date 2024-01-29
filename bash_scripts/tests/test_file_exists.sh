#!/bin/bash

if [ $# -ne 0 ]; then
	if [ -f $1 ]; then
		echo "File $1 exists."
	else
		echo "File $1 can not be found or '[ -f $1 ]' can not be used for checking a file's existence."
	fi
else
	echo "No input argument."
fi
