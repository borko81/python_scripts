mylist = [1, 4, -5, 10, -7, 2, 3, -1]
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

result = (n for n in mylist if n > 0)
print([i for i in result])


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


int_values = filter(is_int, values)
print(list(int_values))