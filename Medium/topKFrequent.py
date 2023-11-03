"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

"""
def topKFrequent(nums, k):
    have = {}
    res = []
    for el in nums:
        if el in have:
            have[el] += 1
        else:
            have[el] = 1
    sorted_have = sorted(have.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(k):
        res.append(sorted_have[i][0])
    return res 


assert topKFrequent([1,1,1,2,2,3], 2) == [1, 2]
assert topKFrequent([9,9,9,9,1,1,1,0,0,0,4,4,10,10,10,10,10], 3) == [10, 9, 1]

