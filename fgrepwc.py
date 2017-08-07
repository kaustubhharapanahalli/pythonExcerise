#!/usr/bin/env python

"fgrepwc.py -- searches for string in text file"

import sys
import string

def usage():
    print "usage: fgrepwc [-i] string filename"
    sys.exit(1)

def fileFind(word, filename):
    count = 0
    try:
        fh = open(filename, 'r')
    except:
        print filename,  ":", sys.exc_info() [1]

    allLines = fh.readlines()
    fh.close()

    for eachLine in allLines:
        if string.find(eachLine, word) > -1:
            count = count + 1
            print eachLine,

    print count

def checkArgs():
    argc = len(sys.argv)
    if argc != 3:
        usage()

    fileFind(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    checkArgs()

  
