#!/usr/bin/env python

def divisionN(a, b):
    q = a // b
    r = a - (q * b)
    return (q, r)

if __name__ == "__main__":
    quo, rem = divisionN(123, 12)
    print quo, rem
