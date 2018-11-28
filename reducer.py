# reducer.py

import operator
import sys

for line in sys.stdin:
    line = line.strip()
    if len(line) > 0:
        block_num_filename, block = line.strip().split('\t',1)
        block_num, filename = block_num_filename.split(',',1)
        print('{}\t{}\t{}'.format(filename, block_num, block))

