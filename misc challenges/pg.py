def validmove(x, y, n):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    return False


def minMoves(n, startX, startY, endX, endY):
    moves, s = [], []
    xm = [-2, -1, 1, 2, -2, -1, 1, 2]
    ym = [-1, -2, -2, -1, 1, 2, 2, 1]

    visit = [[False for i in range(n)] for j in range(n)]

    s.append([startX, startY, 0])
    visit[startX][startY] = True
    while len(s) > 0:
        t = s.pop(0)
        if t[0] == endX and t[1] == endY:
            moves.append(t[2])
        for i in range(8):
            tx = t[0]+xm[i]
            ty = t[1]+ym[i]
            d = t[2]
            if validmove(tx, ty, n) and not(visit[tx][ty]):
                visit[tx][ty] = True
                s.append([tx, ty, d+1])
    return min(moves)


print(minMoves(10, 0, 0, 0, 2))
