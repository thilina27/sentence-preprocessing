#!/bin/bash

timestamp=$(date +%Y_%m_%d_%H%M%S)
if [ ! -d output ]; then
   mkdir output;
fi
if [ ! -d output ]; then
   mkdir output;
fi
cat $1 | python3 mapper.py | sort | python3 reducer.py > output/output_$timestamp.txt
