from collections import namedtuple

Shop = namedtuple('Shop', ['name', 'price', 'anything'])

shop = [
    ('one', 10, 40),
    ('two', 20, 40),
    ('three', 30, 40)
]

for line in shop:
    s = Shop(*line)
    print(s.price)