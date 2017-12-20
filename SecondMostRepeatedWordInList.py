#!/usr/bin/env python
from collections import Counter

def SecondMostRepeated(input):
    dict = Counter(input)
    value = sorted(dict.values(), reverse=True)
    secondLarge = value[1]
    for (key, val) in dict.iteritems():
        if val == secondLarge:
            print key
            return

if __name__ == "__main__":
    input = ["aaa", "bbb", "aaa", "bbb", "aaa", "ccc" ]
    SecondMostRepeated(input)
