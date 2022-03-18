#!/usr/bin/bash
# Script displays size of body of reponse Usage: ./0-body_size.sh 0.0.0.0:5000
curl -sI "$1" | grep 'Content-Length:' | cut -f2 -d' '
