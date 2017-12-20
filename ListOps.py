#!/usr/bin/env python
import sys

if len(sys.argv) != 2:
    print "Supply a file name"
    raise SystemExit(1)

#f = open(sys.argv[1])
#lines = f.readlines()
#f.close()

#fVals = [float(line) for line in lines]
fVals = [float(line) for line in open(sys.argv[1])]
print "Min Val: ", min(fVals)
print "Max Val: ", max(fVals)
