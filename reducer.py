# reducer.py

import operator
import sys

SENTENCE_ENDINGS = ['.', '!', '?', '"']

sentence_count = 0
current_sentence = []

for line in sys.stdin:
    block_num, block = line.strip().split('\t',1)
    print('{}\t{}'.format(block_num, block))

