from collections import defaultdict

data = 'a b a c b a f'.split()

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

d = {}
dd = defaultdict(list)

for item in data:
    if item not in d:
        d[item] = []
    d[item].append(item)


[dd[x].append(x) for x in data]

[print(k, "_".join(v)) for k, v in dict(dd).items()]

min_price = min(zip(prices.values(), prices.keys()))

print(min_price)
print(sorted(zip(prices.values(), prices.keys())))
print(min(prices.items(), key=lambda x: x[1]))