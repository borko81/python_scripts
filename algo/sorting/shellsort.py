def shell_sort(nums):
    gap = len(nums) // 2

    while gap > 0:

        for i in range(gap, len(nums)):
            j = i
            while j >= gap and nums[j - gap] > nums[j]:
                nums[j - gap], nums[j] = nums[j], nums[j - gap]
                j = j - gap

        gap = gap // 2
    return nums


if __name__ == '__main__':
    test = shell_sort([-2, 100, 12, 4, -5])
    print(test)
