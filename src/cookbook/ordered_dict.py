#!/usr/bin/env/ python3
from collections import OrderedDict

d = OrderedDict()
d['Foo'] = 1
d['Bar'] = 2
d['Buzz'] = 3
d['Spam'] = 4

for key in d:
    print(key, d[key])

if __name__ == '__main__':
    print(d)