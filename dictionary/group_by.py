from itertools import groupby
from operator import itemgetter

rows = [
    {'name': "One", "price": 1},
    {'name': "Two", "price": 1},
    {'name': "One", "price": 2},
    {"price": 3, 'name': "One"},
]


rows.sort(key=itemgetter('name'))

print(rows)

for n, p in groupby(rows, key=itemgetter('name')):
    print(n)
    for i in p:
        print(i)