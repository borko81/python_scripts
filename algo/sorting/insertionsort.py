def insertion_sort(nums):
    for i in range(len(nums)):
        j = i

        # check all the previous item
        while j > 0 and  nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1

    return nums


if __name__ == '__main__':
    test = insertion_sort([-2, 100, 12, 4, -5])
    print(test)

