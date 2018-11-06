# reducer.py

import operator
import sys

for line in sys.stdin:
    block_num_filename, block = line.strip().split('\t',1)
    block_num, filename = block_num_filename.split(',',1)
    print('{}\t{}\t{}'.format(block_num, filename, block))

