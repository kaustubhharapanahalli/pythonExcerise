#!/usr/bin/env python

class Complex(object):
    def __init__(self, real, imag=0):
        self.real = float(real)
        self.imag = float(imag)

    def __repr__(self):
        return "Complex(%s, %s)" %(self.real, self.imag)

    def __str__(self):
        return "(%g+%gj)" %(self.real, self.imag)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

if __name__ == "__main__":
    c = Complex(4.0)
    print c + 4.0
