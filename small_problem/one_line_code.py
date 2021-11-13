def is_palindrome(str):
    return str == str[::-1]


nums = [1, 2]
mylist = ['a', 'b', 'c', 'd']
dictionary1 = {"name": "Jack1", "age": 25}
dictionary2 = {"name": "Jack2", "city": "Texas"}
mylist = [1, 5, 8, 'b', 5, 9, 6, 9, 5, 6, 9, 6,
          5, 4, "a", "a", "b", "b", "a", "b", "b"]

print(dict(enumerate(mylist)))

a, b, *c = mylist
print(a, b, c)

[print(x, y) for x in nums for y in mylist]

print(list(zip(nums, mylist)))

print({**dictionary1, **dictionary2})

f = {a: mylist.count(a) for a in mylist}
sorted_f = dict(sorted(f.items(), key=lambda x: -x[1]))
print(sorted_f)
print(dict(enumerate(sorted_f.items())).get(1))

# Next solve
print(max(set(mylist), key=mylist.count))
