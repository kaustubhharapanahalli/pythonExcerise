#!/usr/bin/env python

def factorial(n):
    return n * factorial(n-1) if n > 0 else 1

def factorial_yield(n):
    start = 1
    fact = 1
    while start <= n:
        yield fact
        start = start + 1
        fact = fact * start

Fn = factorial(5)
print "Fact1: %d" % Fn

Fn2 = factorial_yield(5)
for i in Fn2:
    print i
