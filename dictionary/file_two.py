from collections import Counter


# remove duplicates

a = [7, 2, 1, 9, 1, 7, 11, 1]


def found_duplicate(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            

print(list(found_duplicate(a)))
print(Counter(a).most_common(2))