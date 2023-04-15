#!/bin/bash

##############################################
#       FastAPI Consumer setup
##############################################

# turn on bash's job control
set -m

echo "==> FastAPI setup, Start"

echo "==> Environment: Developer"
# FastAPI: Startup
#
# This will start the fastAPI as the primary process and put it in the background
# (Will setup as reload for development purposes)
echo "==> FastAPI startup"
poetry run uvicorn main:app --reload --host 0.0.0.0 --port 5001 &

echo "==> FastAPI setup, Finish ..."


# now we bring the primary process back into the foreground
# and leave it there
fg %1