import string
import timeit

# items = list(string.lowercase)
items = range(1, 10000000)


# def alphabet_generator(items):
#     for i, alphabet in enumerate(items, start=1):
#         yield (i, alphabet)

def number_generator():
    for i in items:
        print(i)
        yield i

def number_iter():
    for i in items:
        print items[i]

gen = number_generator()


def thingy():
    for i in gen:
        print(i)

# thingy()
number_iter()

# print(t2)


# print(next(t))
# print(next(t))

# print(next(it))
# print(next(it))
