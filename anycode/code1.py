p = (4, 5)
x, y = p
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
items = [1, 10, 7, 4, 5, 9]

name, _, _, date = data

name, *any = data


def my_sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head


print(my_sum([1, 2]))
