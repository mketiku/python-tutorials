#!/usr/bin/env python


def simple_generator():
    yield 1
    yield 2
    yield 3


simple_generator()

print(simple_generator)
print(simple_generator())