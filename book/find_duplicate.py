from collections import Counter

a = [1, 7, 2, 9, 7, 11]


def find_fuplicates_in_list(items):
    found_items = set()
    for item in items:
        if item not in found_items:
            yield item
            found_items.add(item)


# print(list(find_fuplicates_in_list(a)))

# Found most looked element
# First using Counter
# print(Counter(a))

# Use dict
data = {x: a.count(x) for x in a}
print(dict(sorted(data.items(), key=lambda x: -x[1])))


# Sorted instance of classes

class User:

    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def __repr__(self):
        return f"{self.__class__.__name__} has id: {str(self.user_id)}"


a1 = User(101)
a2 = User(100)
a3 = User(99)

users = [a1, a2, a3]
print(sorted(users, key=lambda x: x.user_id))