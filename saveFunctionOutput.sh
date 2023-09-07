#!/bin/bash
# tests assignment of function output to a variable inside a bash script

# importing functions from this file
source ../returnChptDirs.sh

# assigning output value of this function 'checkpoint' to a variable 'checkdir'
checkdir=$(checkpoint)
echo checkdir is $checkdir
