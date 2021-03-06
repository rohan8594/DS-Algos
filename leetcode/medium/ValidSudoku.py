# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

# 1. A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# 2. Only the filled cells need to be validated according to the mentioned rules.

# Example 1 : 
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true 

# Example 2 : 
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:
# 1. board.length == 9
# 2. board[i].length == 9
# 3. board[i][j] is a digit or '.'.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidSquare(board)
        
    def isValidRow(self, board):
        for row in board:
            if not self.isValidUnit(row):
                return False
        return True
    
    def isValidCol(self, board):
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False
        return True
    
    def isValidSquare(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValidUnit(square):
                    return False
        return True
    
    def isValidUnit(self, unit):
        array = [c for c in unit if c != '.']
        return len(set(array)) == len(array)