#!/bin/bash

timestamp=$(date +%d_%m_%Y_%H%M%S)
dir=output/job_$timestamp
if [ ! -d output ]; then
   mkdir output;
fi
if [ ! -d output ]; then
   mkdir output;
fi
mkdir $dir
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.13.0.jar \
	-file mapper.py \
	-mapper "/usr/local/bin/python3 mapper.py" \
	-file reducer.py \
	-reducer "/usr/local/bin/python3 reducer.py" \
	-input cs626/project/words.txt \
	-output cs626/project/output
hadoop fs -copyToLocal cs626/project/output/* $dir/
hadoop fs -rm -r cs626/project/output/
