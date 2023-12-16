"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

"""

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])-1
    for i in range(m):
        if matrix[i][0] <= target <= matrix[i][n]:
            first, last = 0, n
            while first <= last:
                mid = (first+last)//2
                if target == matrix[i][mid]:
                    return True
                elif target > matrix[i][mid]:
                    first = mid + 1
                else:
                    last = mid - 1
            return False
    return False

print(searchMatrix([[1]], target = 1))