import random

ar = [random.randint(-1000, 20000) for _ in range(100000)]
# ar = [-10, 7, 3, 8, 10]
# Da se vidi kakvo se generira
# print("-" * 50)
# print(ar)
# print("-" * 50)

without_negative = list(sorted(filter(lambda x: x > 0, ar)))
# Da se vidi sortiraniq list
# print("-" * 50)
# print(without_negative)
# print("-" * 50)

# Vzema min and max ot arr and return new range from them
min, max = without_negative[0], without_negative[-1]
test_array = list(range(min, max + 1))

# found target
found = (set(test_array) ^ set(without_negative))

# return first (min) from found
# print(found.pop())
# Looked be more faster
print(found.pop())
# Also work, but slow before upper, with bigger array system freeze :)
# print(list(sorted([i + 1 for i in ar if i > 0 and i + 1 not in ar])))
