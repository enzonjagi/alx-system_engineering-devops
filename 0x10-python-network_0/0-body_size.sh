#!/usr/bin/env bash
# accepts a URL, sends a request to the URL and returns size of response body
curl "$1" -I -o headers -s
tail -n2 headers | head -n1 |cut '-d ' '-f2'
