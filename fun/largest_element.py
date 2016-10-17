#!/usr/bin/env python3

__project__ = "Find largest element in an array"
__author__ = "Michael Ketiku"


def find_largest(n, A, largest=0):
    '''Find largest element in an array 'A' given the length 'n' of the array'''
    # largest = 0
    if n == 1:
        largest = A[0]
    else:
        find_largest(n-1, A, largest)
        if A[n] > largest:
            largest = A[n]
        return largest

res = find_largest(2,[1,10],0)

print(res)