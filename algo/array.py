array = [10, 3, 7, 5]

array[1] = 30

print(array[:])

# Linnear search O(N)
max = array[0]

for num in array:
    if num > max:
        max = num

print(max)
