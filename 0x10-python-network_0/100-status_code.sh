#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code
curl -sI $1 | head -n 1 | cut -d ' ' -f2
