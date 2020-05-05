#!/bin/sh

if [[ $OSTYPE =~ "darwin" || $OSTYPE =~ "linux" ]]
then # macos/linux
    which python | grep ".env" >/dev/null 2>&1 && return 0
    if [[ $(python3 --version | cut -d ' ' -f 2 | cut -d '.' -f 1-2) != "3.8" ]]
    then
        echo "python 3.8+ required!\n"
        return 1
    fi
    python3 -c "import virtualenv" >/dev/null 2>&1 || sudo python3 -m pip install virtualenv
    if [[ -d ".env" ]]
    then # env exists
        echo "activating virtualenv"
        source .env/bin/activate
    else # create env
        echo "creating virtualenv\n"
        virtualenv .env
        echo "activating virtualenv\n"
        source .env/bin/activate
        echo "installing requirements"
        pip install -r requirements.txt
    fi
else # windows
    which py | grep ".env" >/dev/null 2>&1 && return 0
    if [[ $(py --version | cut -d ' ' -f 2 | cut -d '.' -f 1-2) != "3.8" ]]
    then
        echo "python 3.8+ required!\n"
        return 1
    fi
    py -c "import virtualenv" >/dev/null 2>&1 || py -m pip install virtualenv
    if [[ -d ".env" ]]
    then # env exists
        echo "activating virtualenv"
        source .env/scripts/activate
    else # create env
        echo "creating virtualenv\n"
        py -m virtualenv .env
        echo "activating virtualenv\n"
        source .env/scripts/activate
        echo "installing requirements"
        py -m pip install -r requirements.txt
    fi
fi

