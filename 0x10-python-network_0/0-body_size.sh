#!/bin/bash
# Bash script that takes in a URL
curl "$1" -sI |grep "Content-Length"| cut -d ':' -f 2 | cut -d ' ' -f 2
