#!/bin/bash
# Sends a JSON to a given URL with a given JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
