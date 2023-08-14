#!/bin/bash

watch_this_file="../logfile.txt"

echo $watch_this_file | entr bash test_log_alert.sh 


