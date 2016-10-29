#!/bin/python3

import sys


# n = int(input().strip())
# a = []
# for a_i in range(n):
#     a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
#     a.append(a_t)
n = 3
a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]


# def abs_difference(*args):
#     print(*args)
#     pass

# # diagonal = [[x for x in row] for row in a]
# # print(diagonal)


# def get_diagonal(*args):
#     total = 0 
#     for matrix in args:
#         for y, row in enumerate(matrix):
#             # total = 0
#             # print(row[1])
#             # for x in range(0, len(row), 2):
#             #     total += x 
#             #     print(total)
#             for x in row[::1]:
#                 total += x
#             # for i, x in enumerate(row):
#             #     if x == 1:
#             #         total += x
#                 print(total)
#             print(row)
#     # return
#     return(row)

# get_diagonal(a)
# # abs_difference(a)
def diagonal_diff(matrix):
    l = sum(row[i] for i, row in enumerate(matrix))
    difference = sum(row[i] - row[-i-1] for i, row in enumerate(matrix))
    return abs(difference)
print(diagonal_diff(a))