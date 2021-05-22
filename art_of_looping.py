import itertools

some_text = 'YAaANNGGg'
my_list = [1, 9, 3, 4, 2, 5]

for key, group in itertools.groupby(some_text, lambda x: x.upper()):
    print(key, list(group))


print("_".join(sorted([str(x) for x in my_list if not x & 2], key=lambda x: x, reverse=True)))


def fibo(n):
    x, y = 0, 1
    while y < n:
        x, y = y, x + y
        yield x

print([x for x in fibo(50)])