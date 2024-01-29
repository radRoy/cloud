#!/bin/bash

# a test
if [ $# -eq 0 ]
then
	echo "No arguments supplied"
else
	echo "Argument supplied: ${1}"
fi

# testing 'if not'
if ! [ $# -eq 0 ]
then
	echo "Argument supplied: ${1}"
else
	echo "No arguments supplied"
fi

# testing 'if not' inside the brackets
if [ ! $# -eq 0 ]
then
        echo "Argument supplied: ${1}"
else
        echo "No arguments supplied"
fi
