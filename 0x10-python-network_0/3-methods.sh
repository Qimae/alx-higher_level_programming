#!/bin/bash
# Script takes URL and displays all HTTP methods
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' ' 
