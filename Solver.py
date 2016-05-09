#!/usr/bin/env python #implicitly runs the file as a script
import math
'''
This application computes the roots of a polynomial function.

'''
__author__ = "Michael Ketiku"
__project__ = "MySimplePythonApplication"
___email__ = "mketiku@gmail.com"
___status__ = "final"


class Solver:
	# a@staticmethod
	def __init__(self):
		while True:
			a = int(input("a "))
			b = int(input("b "))
			c = int(input("c "))
			d = ((b ** 2) - (4 * a * c))
			if d >= 0:
				disc = math.sqrt(d)
				root1 = (-b + disc) / (2 * a)
				root2 = (b + disc) / (2 * a)
				print(root1, root2)
			else:
				print("error")
Solver().__init__()
