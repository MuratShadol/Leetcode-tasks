"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

"""

def twoSum(nums, target):
    have = {}
    for i, el in enumerate(nums):
        if target - el in have:
            return [have[target-el], i]
        else:
            have[el] = i
    

assert twoSum([1, 2, 3, 3], 6) == [2, 3]
assert twoSum([4, 1, 0, 7, 10], 14) == [0, 4]
assert twoSum([7, 4, -6, 2, -10], -16) == [2, 4]