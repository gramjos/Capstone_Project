#!/usr/bin/bash

cmd () {
if ! tail -n14 ../logfile.txt | grep '200 OK' -q
then 
  python3 email_attach.py
fi
}

cmd
