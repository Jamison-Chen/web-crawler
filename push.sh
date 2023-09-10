#!/bin/bash
if [[ -z $1 ]]; then
    echo Please provide the commit message.
else
    pipenv requirements >requirements.txt
    git add .
    git commit -m "$1"
    git push -u origin master
fi
