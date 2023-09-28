#!/bin/bash
# Get the URL from the command line argument
curl -s "$1" | wc -c
