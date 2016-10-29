#!/usr/bin/env python3

'''
Computing exponentials using recursion
'''

__project__ = "Calculate exponents using recursion"
__author__ = "michael ketiku"


def compute_exponent(a, n):
    '''Computes the exponent of 'a' given 'n' '''
    if n <= 1:
        return a
    else:
        return (a * compute_exponent(a, n - 1))

res = compute_exponent(10, 2)
print(res)
