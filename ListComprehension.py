#!/usr/bin/env python

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
U = [x for x in S if x % 2 == 0]

print S
print V
print U
