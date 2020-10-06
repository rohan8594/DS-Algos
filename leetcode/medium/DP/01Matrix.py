# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.
# Example 1:
# Input:

# 0 0 0
# 0 1 0
# 0 0 0
# Output:
# 0 0 0
# 0 1 0
# 0 0 0
# Example 2:
# Input:

# 0 0 0
# 0 1 0
# 1 1 1
# Output:
# 0 0 0
# 0 1 0
# 1 2 1

# Note:
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.


class Solution:
    def updateMatrix(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != 0:
                    matrix[i][j] = float('inf')
                    if i > 0:
                        matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j])
                    if j > 0:
                        matrix[i][j] = min(matrix[i][j - 1] + 1, matrix[i][j])

        for i in range(len(matrix) - 1, -1, -1):
            for j in range(len(matrix[0]) - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i < len(matrix) - 1:
                        matrix[i][j] = min(matrix[i + 1][j] + 1, matrix[i][j])
                    if j < len(matrix[0]) - 1:
                        matrix[i][j] = min(matrix[i][j + 1] + 1, matrix[i][j])
        return matrix
