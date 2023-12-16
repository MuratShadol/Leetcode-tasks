"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

"""

def search(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = (start+end)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid+1
        else:
            end = mid-1
    return -1


assert search([1, 2, 3, 4, 5, 10], 2) == 1
assert search([1, 3, 4, 5, 7, 8], 8) == 5
assert search([-4, -2, -1, 0, 1, 3, 6], -10) == -1
assert search([-4, -2, -1, 0, 1, 3, 6], 10) == -1