items = [1, 2, [3, 4, [5, 6], 7], 8]

listOfList = [ [1, 2, 3, 4, 5],
                [11, 22, 33, 44, 55],
                [17, 18, 19, 20, 21] ]

result = []

# Not work as i think

def check_is_list(items):
    global result
    if isinstance(items, list):
        result.extend(items)
    else:
        result.append(items)
    return result


for x in items:
    check_is_list(x)


print(result)