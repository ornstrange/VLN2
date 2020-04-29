#!/bin/sh

# set correct path based on os
[[ $OSTYPE =~ "(darwin|linux-gnu)" ]] && path=".env/bin/activate" || path=".env/scripts/activate"

# create virtual environment, activate and install dependencies if run for first time, else activate it
[[ -d ".env" ]] && source .env/bin/activate || virtualenv .env ; source .env/bin/activate ; pip install -r requirements.txt

