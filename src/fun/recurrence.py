#!/usr/bin/env python3

from math import log


def t(n):
    '''Returns the recurrence solution for an integer n'''
    if n == 1:
        return 1
    elif n % 2 == 0:
        return (t(n / 2)) + (log(n))
    elif n < 1:
        return 0
    else:
        print("Invalid Input: (n) must be a multiple of 2")
        return n


def main():
    print(t(4))
    # for i in range(0, 11, 2):

# print(i)


if __name__ == '__main__':
    main()
