from collections import namedtuple
data = []

Subscribe = namedtuple('Subscribe', 'name age'.split())

response = [('first', 10), ('second', 20), ('last', 30)]

for name, age in response:
    s = Subscribe(name, age)
    data.append(s)


for i in data:
    print(i.name, i.age)