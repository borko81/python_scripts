from itertools import groupby

data = [
    {'name': 'First', 'age': 3},
    {'name': 'Second', 'age': 10},
    {'name': 'Third', 'age': 3},
    {'name': 'Four', 'age': 4}
]

data.sort(key=lambda x: x['age'])

for name, age in groupby(data, key=lambda x: x['age']):
    print(f'{name} {"-" * 10}')
    for a in age:
        print('\t', a)


# Filter elements
def check_element_is_valid(val):
    try:
        _ = int(val)
    except ValueError:
        return False
    else:
        return True


l = [1, 6, -4, 12, -7, 2, 9, -1, '-', 'N/A']
l = list(filter(check_element_is_valid, l))

for x in (_ for _ in l if _ > 0):
    print(x, end=' ')
