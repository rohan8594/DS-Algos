# Given a board of 0's (Path) and -1 (Wall), and an end position (x, y), return true if there is a path
# from every 0 on the board to the end position, and return false if there is any 0 on the board from
# where you can't reach the end position

# Note there is one constraint - you can't modify the board itself


def boardGame(board, pos):
    x, y = pos
    boardcpy = board

    dfs(board, boardcpy, x, y)

    for i in range(len(boardcpy)):
        for j in range(len(boardcpy[0])):
            if boardcpy[i][j] == 0:
                return False
    return True


def dfs(board, boardcpy, i, j):
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != 0:
        return

    boardcpy[i][j] = "#"
    dfs(board, boardcpy, i + 1, j)
    dfs(board, boardcpy, i, j + 1)
    dfs(board, boardcpy, i - 1, j)
    dfs(board, boardcpy, i, j - 1)


# Test Cases
board1 = [[0, 0, 0, 0],
          [0, -1, -1, 0],
          [-1, 0, 0, 0],
          [0, -1, 0, 0]]

board2 = [[0, 0, 0, 0],
          [0, -1, -1, 0],
          [-1, 0, 0, 0],
          [0, 0, 0, 0],
          [0, -1, 0, -1]]

endPos = (0, 0)

print(boardGame(board1, endPos))
print(boardGame(board2, endPos))
