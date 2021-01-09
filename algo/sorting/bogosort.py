import random
from typing import List


class BogoSort:

    def __init__(self, nums: List):
        self.nums = nums
        self.counter: int = 0

    def sort(self) -> None:
        while not self.is_sorted():
            self.counter += 1
            print("Shuffle again {}".format(self.counter))
            self.shuffle()

    def shuffle(self) -> None:
        for i in range(len(self.nums) - 2, -1, -1):
            j = random.randint(0, i + 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def is_sorted(self) -> bool:
        for i in range(len(self.nums) - 1):
            if self.nums[i] > self.nums[i + 1]:
                return False
        return True


if __name__ == '__main__':
    alg = BogoSort([1, -4, 0, 2, 6, 0, 10])
    alg.sort()
    print(alg.nums)
