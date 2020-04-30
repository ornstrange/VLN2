#!/bin/sh

# set correct python interpreter and path, based on os
(command -v python3 >/dev/null 2>&1 &&\
    { py="sudo python3" ; activatepath=".env/bin/activate" }) ||\
(command -v py3 >/dev/null 2>&1 &&\
    { py="py3" ; activatepath=".env/scripts/activate" }) ||\
{ echo "python 3 required..." ; exit }

# install virtualenv if it doesn't exist
command -v virtualenv >/dev/null 2>&1 ||\
    { echo "installing virtualenv...\n" ; $py -m pip install virtualenv }

# create virtual environment, activate and install dependencies
# if run for first time, else activate it
stat ".env" >/dev/null 2>&1 &&\
    source $activatepath ||\
    { echo "creating virtualenv...\n" ; virtualenv .env ;\
        source $activatepath ; pip install -r requirements.txt }

echo "virtualenv activated\n"

