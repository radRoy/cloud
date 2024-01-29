#!/bin/bash

f_prompt_yn () {  # credit goes to https://stackoverflow.com/a/12202793
    while true; do
        read -p "$1 " yn
        case $yn in
            [Yy]* ) return 0;;
            [Nn]* ) return 1;;
            * ) echo "Please answer yes or no.";;
        esac
    done
}