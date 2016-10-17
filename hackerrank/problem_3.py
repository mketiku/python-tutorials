#!/usr/bin/env python3

'''
https://www.hackerrank.com/challenges/compare-the-triplets
'''


import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]


class Problem(object):
    '''Describes a problem for Hackerrank.'''

    def __init__(self, name, rating, category, point):
        self.name = name
        self.category = category
        if rating is None:
            self.rating = []
        else:
            self.rating = rating
        if point is None:
            self.point = 0
        else:
            self.point = point

    def add_rating(self, value):
        '''Add a rating to a Problem'''
        if value not in self.rating:
            self.rating.append(value)

    def compare_score(self, other):
        '''Compare the score of one problem to another'''
        for (val1, val2) in zip(self.rating, other.rating):
            if val1 > val2:
                self.point += 1
            elif val1 < val2:
                other.point += 1
        return(self.point, other.point)

    def __repr__(self):
        '''Representation of a problem to recreate the object'''
        return "Problem('{}', '{}', '{}')".format(
            self.name, self.category, self.rating)

    # def __str__(self):
    #     '''Representation of a problem to recreate the object'''
    #     _lead = "An instance of class Problem with state: "
    #     return  _lead + "('{}', '{}', '{}')".format(
    #         self.name, self.category, self.rating)

    def __str__(self):
        '''String Representation of a problem class'''
        return str(self.__class__) + ": " + str(self.__dict__)


A = Problem("Q1", [5, 6, 7], "Criticism", None)
B = Problem("Q2", [3, 6, 10], "Originality", None)


# Alternate way 
# arr1 = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# arr2 = [int(arr_temp) for arr_temp in input().strip().split(' ')]


arr1 = [a0,a1,a2]
arr2 = [b0,b1,b2]

A.rating = arr1
B.rating = arr2

final_result = Problem.compare_score(A, B)

res = str(final_result[0]) + " " + str(final_result[1])
print(res)