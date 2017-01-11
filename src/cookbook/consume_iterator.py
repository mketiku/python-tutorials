import string

items = list(string.lowercase)


def alphabet_generator(items):
    for i, alphabet in enumerate(items, start=1):
        yield (i, alphabet)


it = iter(alphabet_generator(items))


t = alphabet_generator(items)

print(next(t))
print(next(t))
print(next(t))

print(next(it))
print(next(it))
