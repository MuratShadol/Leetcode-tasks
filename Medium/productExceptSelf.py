"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
"""

def productExceptSelf(nums):
    prefixR = [1]*len(nums)
    prefixL = [1]*len(nums)
    for i in range(1, len(nums)):
        prefixR[i] = nums[i-1] * prefixR[i-1]
    
    for i in range(len(nums)-2, -1, -1):
        prefixL[i] = nums[i+1] * prefixL[i+1]
    
    for i in range(len(nums)):
        nums[i] = prefixL[i]*prefixR[i]
    return nums


assert productExceptSelf([1,2,3,4]) == [24,12,8,6]
assert productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]