#!/usr/bin/env python

def print_matcher(matchtext):
    print "Looking for", matchtext
    while True:
        line = (yield)
        if matchtext in line:
            print line

if __name__ == "__main__":
    matchers = [
               print_matcher("python"),
               print_matcher("jython"),
               print_matcher("guido")
               ]
    for m in matchers:
        m.next()
