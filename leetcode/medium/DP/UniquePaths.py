# A robot is located at the top-left corner of a m x n grid (marked
# Start' in the diagram below).

# The robot can only move either down or right at any point in time. The
# robot is trying to reach the bottom-right corner of the grid (marked
# 'Finish' in the diagram below).

# How many possible unique paths are there?


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid = [[1] * m] * n
        grid = [[1] * m for _ in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[n - 1][m - 1]
