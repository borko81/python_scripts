from typing import List


def selection_sort(data: List) -> List:
    for i in range(len(data) - 1):
        # store the index of min item
        index: int = i

        # linear search O(N)
        for j in range(i, len(data)):
            if data[j] < data[index]:
                index = j

        # swap position
        if index != i:
            data[index], data[i] = data[i], data[index]

    return data


if __name__ == '__main__':
    test = selection_sort([-2, 100, 12, 4, -5])
    print(test)
