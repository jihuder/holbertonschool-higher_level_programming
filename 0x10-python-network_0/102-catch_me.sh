#!/bin/bash
# Script to make a request to receive a custom message as response
curl -sL -XPUT -H "Origin:You got me!" -d "X-School-User-Id=98" "0.0.0.0:5000/catch_me"
