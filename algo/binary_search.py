from typing import BinaryIO


def binary_search(arr, low, hight, x):
    if hight >= low:
        mid = (hight + low) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, hight, x)
    return -1


arr = [2, 3, 4, 10, 40]
x = 11
result = binary_search(arr, 0, len(arr)-1, x)
if result != -1:
    print(str(result))
else:
    print("element not found")
