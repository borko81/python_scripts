prices = {
    "Book1": 75.13,
    "Book2": 61.38,
    "Book3": 95.57,
    "Book4": 87.10,
    "Book5": 40.79
}

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 5,
    'x': 4,
    'y': 4
}

# found min price
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
min_price_two = min(prices, key=lambda x: x[1])

# print(min_price)
# print(max_price)
# print({min_price_two, prices[min_price_two]})

print(a.keys() - b.keys())
print(a.keys() & b.keys())
print(a.keys() ^ b.keys())
print({**a, **b})
print({k: a[k] for k in a.keys() - {'z'}})