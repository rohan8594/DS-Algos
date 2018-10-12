# Given a m x n matrix, if an element is 0, set its entire row and column 
# to 0. Do it in-place.

# Example 1:

# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        firstRow = False
        firstCol = False
        rows = len(matrix)
        cols = len(matrix[0])

        # check for zero in first column
        for i in range(rows):
          if matrix[i][0] == 0:
            firstCol = True
            break

        # check for zero in first row
        for j in range(cols):
          if matrix[0][j] == 0:
            firstRow = True
            break

        # check for zeroes in rest of the matrix
        for i in range(1, rows):
          for j in range(1, cols):
            if matrix[i][j] == 0:
              matrix[i][0] = 0
              matrix[0][j] = 0

        # nullify rows and columns based on values stored
        # in first row and coulmn
        for i in range(1, rows):
          for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
              matrix[i][j] = 0

        # nullify first column if needed
        if firstCol == True:
          for i in range(rows):
            matrix[i][0] = 0

        # nullify first row if needed
        if firstRow == True:
          for j in range(cols):
            matrix[0][j] = 0
