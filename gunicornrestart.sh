#!/bin/bash
kill ="pkill gunicorn"
printf "%s\n" $kill
eval $kill
cmd="gunicorn -c ~/CSC394Project/config/gunicorn/dev.py"
printf "%s\n" $cmd
eval $cmd
