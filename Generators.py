#!/usr/bin/env python

def countDown(n):
    print "Counting Down!"
    while n > 0:
        yield n
        n = n-1

if __name__ == "__main__":
    for c in countDown(5):
        print c,
