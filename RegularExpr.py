#!/usr/bin/env python

import re

def extract(input):
    count = 0
    substr = re.search('10+1', input)
    while substr != None:
        count = count + 1
        input = input[(substr.end()-1):]
        substr = re.search('10+1', input)
    print count

if __name__ == "__main__":
    input = '1101001010010111'
    extract(input)
