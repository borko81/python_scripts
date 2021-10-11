import heapq

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

small = heapq.nsmallest(3, portfolio, key=lambda x: x['price'])

bigger = sorted(
    heapq.nlargest(3, portfolio, key=lambda x: x['price']),
    key=lambda x: x['price']
)

[print(x) for x in bigger]
