#!/bin/sh

# set correct python
command -v python3 >/dev/null 2>&1 &&\
    py=python3 ||\
    command -v py3 >/dev/null 2>&1 &&\
    py=py3

# set correct path based on os
[[ $OSTYPE =~ "(darwin|linux-gnu)" ]] &&\
    activatepath=".env/bin/activate" ||\
    activatepath=".env/scripts/activate"

# install virtualenv if it doesn't exist
command -v virtualenv >/dev/null 2>&1 &&\
    echo "virtualenv installed" ||\
    sudo $py -m pip install virtualenv

# create virtual environment, activate and install dependencies
# if run for first time, else activate it
stat ".env" >/dev/null 2>&1 &&\
    source $activatepath ||\
    virtualenv .env; source $activatepath; pip install -r requirements.txt

