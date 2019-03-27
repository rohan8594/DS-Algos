# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# Example:

# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Explanation:

# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
import collections


class Solution:
    def solve(self, board: 'list[list[str]]') -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        rows, cols = len(board), len(board[0])
        queue = collections.deque([])

        for i in range(rows):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][cols - 1] == 'O':
                queue.append((i, cols - 1))

        for j in range(cols):
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[rows - 1][j] == 'O':
                queue.append((rows - 1, j))

        while queue:
            i, j = queue.popleft()

            if 0 <= i < rows and 0 <= j < cols and board[i][j] == 'O':
                board[i][j] = '#'
                queue.append((i - 1, j))
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '#':
                    board[i][j] = 'O'
