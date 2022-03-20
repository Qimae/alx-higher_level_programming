#!/bin/bash
# Script sends POST request to URL and displays response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
