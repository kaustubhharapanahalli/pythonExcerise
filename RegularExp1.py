#!/usr/bin/env python

import re

regex = r"([a-zA-Z]+) (\d+)"
#        r"([a-zA-Z]+) (\d+)"
if re.search(regex, "June 24"):
    match = re.search(regex, "June 24")
    print "Match at index %s, %s" % (match.start(), match.end())
    print "Full match %s" % match.group(0)
    print "Month: %s" % match.group(1)
    print "Day: %s" % match.group(2)
else:
    print "the regex pattern does not match..."

print re.sub(regex, r"\2 of \1", "June 24, Dec 14, Aug 15")
