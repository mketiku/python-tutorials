#!/usr/bin/env python3


def array_left_rotation(a, n, k):
    pivot = a[0]
    for i in range(n):
        print(a)
        a[i] = a[i+1]
        print(a) 
        print(a[i])
    return(a)
# answer= list[1,2]

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);

# print(*answer, sep=' ')