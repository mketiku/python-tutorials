#!/usr/bin/env/ python3
import math



def unpack(grade):
    '''Unpacks Elements from Iterables of Arbitrary Length''''
    first, *middle, last = grade
    return sum(middle)


if __name__ == '__main__':
    grade = ['Michael', 2,3,4,5,'Ketiku']
    res = unpack(grade)
    print(res)
