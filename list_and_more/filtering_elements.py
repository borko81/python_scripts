import random

elements = [random.randint(-100, 100) for _ in range(1, 20)]
nums = ['1', '2', -1, 'N/A', '-']

print(elements)

# with list
# positive_elements = [i for i in elements if i > 0]

# with generator
positive_elements = (i for i in elements if i > 0)

print(positive_elements)


def is_int(el):
    try:
        x = int(el)
        return True
    except ValueError:
        return False
    
    
print([x for x in nums if is_int(x)])
print(list(filter(is_int, nums)))
    