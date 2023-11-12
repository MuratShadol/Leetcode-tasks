"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""


def maxArea(height):
    first = 0
    last = len(height) - 1
    area = 0
    max_area = 0

    while first < last:
        area = min(height[first], height[last]) * (last - first)
        if area > max_area:
            max_area = area
        if height[first] < height[last]:
            first += 1
        else: 
            last -= 1
    return max_area


assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
