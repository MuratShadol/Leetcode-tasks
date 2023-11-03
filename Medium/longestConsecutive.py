"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.

"""


def longestConsecutive(nums):
    set_nums = set(nums)
    length = 0
    res = []
    for i in range(len(nums)-1):
        temp = nums[i+1]-nums[i]
        if temp in set_nums and temp == 1:
            length += 1
        else:
            res.append(length)
    return res, length


print(longestConsecutive([100,4,200,1,3,2]))