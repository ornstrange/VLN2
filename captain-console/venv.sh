#!/bin/sh

[[ -d ".env" ]] && source .env/bin/activate || virtualenv .env

