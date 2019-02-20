#
# Complete the 'roverMove' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER matrixSize
#  2. STRING_ARRAY cmds
#


def roverMove(matrixSize, cmds):
    # Write your code here
    rover = 0
    i, j = 0, 0

    for cmd in cmds:
        if cmd == "RIGHT":
            if j < matrixSize - 1:
                j += 1
        if cmd == "LEFT":
            if j > 0:
                j -= 1
        if cmd == "UP":
            if i > 0:
                i -= 1
        if cmd == "DOWN":
            if i < matrixSize - 1:
                i += 1
    return (i * matrixSize) + j
