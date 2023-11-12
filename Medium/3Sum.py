"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

"""


def threeSum(nums):
    nums = sorted(nums)
    result = []
    for i in range(len(nums)):
        target = -nums[i]
        if i != 0 and target == -nums[i-1]:
            continue
        j = i+1
        k = len(nums) - 1
        
        while j < k:
            if nums[j] + nums[k] == target:
                if i > 0 and k < len(nums)-1:
                    if nums[j] != nums[j-1] or nums[k] != nums[k+1]:    
                        result.append([nums[i], nums[j], nums[k]])
                else:
                    result.append([nums[i], nums[j], nums[k]])
                k -= 1
                j += 1
            elif nums[j] + nums[k] > target:
                k -= 1
            else:
                j += 1
    return result


            