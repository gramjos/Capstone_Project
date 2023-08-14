#!/bin/bash
source /home/ubuntu/project/bin/activate
cmd="http GET http://3.135.236.213/ --header >> ~/CSC394Project/logfile.txt"
eval $cmd 

