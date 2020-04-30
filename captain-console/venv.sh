#!/bin/sh

if [[ $OSTYPE =~ "(darwin|linux-gnu)" ]]
then # macos/linux
    which python | grep ".env" >/dev/null 2>&1 && return 0
    if [[ $(python --version | cut -d ' ' -f 2 | cut -d '.' -f 1-2) != "3.8" ]]
    then
        echo "python 3.8+ required!\n"
        return 1
    fi
    if [[ ! $(python -c "import virtualenv" >/dev/null 2>&1) ]]
    then # virtualenv not installed
        echo "installing virtualenv\n"
        sudo pip install virtualenv
    fi
    if [[ -d ".env" ]]
    then # env exists
        echo "activating virtualenv\n"
        source .env/bin/activate
    else # create env
        echo "creating virtualenv\n"
        virtualenv .env
        echo "activating virtualenv\n"
        source .env/bin/activate
        echo "installing requirements\n"
        pip install -r requirements.txt
    fi
else # windows
    which py | grep ".env" >/dev/null 2>&1 && return 0
    if [[ $(py --version | cut -d ' ' -f 2 | cut -d '.' -f 1-2) != "3.8" ]]
    then
        echo "python 3.8+ required!\n"
        return 1
    fi
    if [[ ! $(py -c "import virtualenv" >/dev/null 2>&1) ]]
    then # virtualenv not installed
        echo "installing virtualenv\n"
        py -m pip install virtualenv
    fi
    if [[ -d ".env" ]]
    then # env exists
        echo "activating virtualenv\n"
        source .env/bin/activate
    else # create env
        echo "creating virtualenv\n"
        py -m virtualenv .env
        echo "activating virtualenv\n"
        source .env/bin/activate
        echo "installing requirements\n"
        py -m pip install -r requirements.txt
    fi
fi

