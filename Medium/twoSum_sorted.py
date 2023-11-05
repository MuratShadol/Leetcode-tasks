"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. 
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

"""

def twoSum(nums, target):
    first = 0
    last = len(nums) - 1

    while first < last:
        result = nums[first] + nums[last]
        if target == result:
            return [first+1, last+1]
        elif result > target:
            last -= 1
        else:
            first += 1


assert twoSum([2, 4, 5, 8, 9, 18], 9) == [2, 3]
assert twoSum([1, 2, 4, 6, 8, 9, 13], 14) == [1, 7]
assert twoSum([-9, -8, -6, 4], -15) == [1, 3]