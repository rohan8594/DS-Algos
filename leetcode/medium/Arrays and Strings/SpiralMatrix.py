# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# Example 1:

# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:

# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Note: Not all test cases passing


class Solution:
    def spiralOrder(self, grid: 'List[List[int]]') -> 'List[int]':
        if not grid:
            return []

        rows, cols = len(grid), len(grid[0])
        res, n = [], 0

        while n <= rows // 2:
            for j in range(n, cols - n):
                res.append(grid[n][j])

            for i in range(1 + n, rows - n):
                res.append(grid[i][cols - 1 - n])

            for j in range(cols - 2 - n, -1 + n, -1):
                res.append(grid[rows - 1 - n][j])

            for i in range(rows - 2 - n, 0 + n, -1):
                res.append(grid[i][n])
            n += 1

        return res
