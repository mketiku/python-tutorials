#!/usr/bin/env/ python3

D = {
    "Foo": 1,
    "Bar": 2,
    "Buzz": 3,
    "Bin": 4,
    "Marco": 5,
}

D_zipped = zip(D.values(), D.keys())
print(D.keys(), D.values())
print(D_zipped)
print(min(D_zipped))
