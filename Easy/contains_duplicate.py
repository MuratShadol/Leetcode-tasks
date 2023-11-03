"""
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

"""

def containsDuplicate(nums):
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        else:
            seen[nums[i]] = i
    return False


def containsDuplicate2(nums):
    seen = set()
    
    for i in nums:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False


assert containsDuplicate([1, 2, 2, 4]) == True
assert containsDuplicate([1, 2, 3, 1]) == True
assert containsDuplicate([0, 1, 3, 4]) == False

assert containsDuplicate2([1, 2, 2, 4]) == True
assert containsDuplicate2([1, 2, 3, 1]) == True
assert containsDuplicate2([0, 1, 3, 4]) == False