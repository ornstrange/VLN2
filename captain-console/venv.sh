#!/bin/sh

[[ -d ".env" ]] && source .env/bin/activate || virtualenv .env ; source .env/bin/activate ; pip install -r requirements.txt

