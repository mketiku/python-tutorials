#!/usr/bin/env python

import string
import math


alphabet_list = list(string.lowercase)
number_list = range(1, 100)

# for alphabet in alphabet_list:
#     print alphabet

# print(alphabet_list)
# print(number_list)


# def get_primes(input_list):
#     result_list = []
#     for element in input_list:
#         if is_prime(element):
#             result_list.append(element)

#     return result_list

    
# def is_prime(number):
#     if number > 1:
#         if number == 2:
#             return True
#         if number % 2 == 0:
#             return False
#         for current in range(3, int(math.sqrt(number) + 1), 2):
#             if number % current == 0:
#                 return False
#         return True
#     return False


# res = get_primes(number_list)
# print(res)


def simple_generator():
   while True:
       yield number 


our_generator = simple_generator()
