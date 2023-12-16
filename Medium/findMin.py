"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

"""

def findMin(nums):
    start, end = 0, len(nums)-1
    res = nums[0]
    while start <= end:
        if nums[start] <= nums[end]:
            return min(res, nums[start])
        mid = (start+end)//2
        res = min(res, nums[mid])
        if nums[mid] >= nums[start]:
            start = mid + 1
        else:
            end = mid - 1
                

# assert findMin([3,4,5,1,2]) == 1
# assert findMin([4,5,6,7,0,1,2]) == 0
# assert findMin([11,13,15,17]) == 11
assert findMin([5, 1, 2, 3, 4]) == 1