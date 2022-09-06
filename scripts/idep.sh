#!/usr/bin/env bash
BASEDIR=$(basename "$0")
PARANTDIR=$(dirname "$BASEDIR")

python3 -m venv $PARANTDIR/venv
source $PARANTDIR/venv/bin/activate
pip install -r requirements.txt
