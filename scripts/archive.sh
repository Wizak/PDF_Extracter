#!/usr/bin/env bash
BASEDIR=$(basename "$0")
PARANTDIR=$(dirname "$BASEDIR")

git archive --output=$PARANTDIR/extracter_example.zip --format=zip HEAD
