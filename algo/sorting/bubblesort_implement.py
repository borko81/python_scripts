from typing import List


class BubbleSort:

    def __init__(self, nums: List):
        self.nums = nums

    def ascending_sort(self):
        for i in range(len(self.nums) - 1):
            for j in range(len(self.nums) - i - 1):
                if self.nums[j] > self.nums[j + 1]:
                    self.swap(j, j + 1)

    def descending_sort(self):
        for i in range(len(self.nums) - 1):
            for j in range(len(self.nums) - 1 - i):
                if self.nums[j] < self.nums[j + 1]:
                    self.swap(j, j + 1)

    def swap(self, i, j):
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]


if __name__ == '__main__':
    test = BubbleSort([1, -6, -2, 10, 11, 100, 99, 2])
    test.descending_sort()
    print(test.nums)
