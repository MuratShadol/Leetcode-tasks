"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

"""

def trap(height):
    id_top = height.index(max(height))
    first = 0
    water = 0
    last = len(height) - 1
    current_max = height[first]
    while first <= id_top:
        if height[first] > current_max:
            current_max = height[first]
        else:
            water += current_max - height[first]
        first += 1

    current_max = height[last]
    while last >= id_top:
        if height[last] > current_max:
            current_max = height[last]
        else:
            water += current_max - height[last]
        last -= 1

    return water

    
assert trap([4,2,0,3,2,5]) == 9
assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6