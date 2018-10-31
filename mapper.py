# mapper.py

import sys

SENTENCE_ENDINGS = ['.', '!', '?', '"']
ABBREVIATIONS = ['mr.', 'mrs.', 'ms.', 'jr.', 'sr.', 'dr.']

block_count = 0
curr_block = []

for line in sys.stdin:
    line = ' '.join(line.strip().split()[1:]).lower()
    if len(line) == 0:
        # Skip empty lines, TODO: something else here?
        continue
    in_single_sentence = False
    if len(curr_block) == 0:
        curr_block = [line]
        in_single_sentence = True
    elif line[0] == '"':
        # End the previous block
        print('{}\t{}'.format(block_count, ' '.join(curr_block)))
        curr_block = [line]
        block_count += 1
        in_single_sentence = True
    # Check if this line ends a sentence
    if line[-1] in SENTENCE_ENDINGS:
        # Check that it's not a period and one of our abbreviations
        if line[-1] == '.' and line.split()[-1] in ABBREVIATIONS:
            # Remove the period
            line = line[:-1]
            # Add line to block and continue to next iteration
            curr_block.append(line)
            continue
        # End the current block
        if not in_single_sentence:
            # Because we've already added this line to curr_block
            curr_block.append(line)
        print('{}\t{}'.format(block_count, ' '.join(curr_block)))
        curr_block = []
        block_count += 1
    elif not in_single_sentence:
        curr_block.append(line)
