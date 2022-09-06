#!/usr/bin/env bash
BASEDIR=$(basename "$0")
PARANTDIR=$(dirname "$BASEDIR")

source $PARANTDIR/venv/bin/activate
python $PARANTDIR/main.py
