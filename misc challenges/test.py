def foo(a):
    for y in range(0, 4):
        for x in range(0, 4):
            if x < 3:
                if a[x+1][y] != None:
                    if a[x+1][y] == a[x][y]:
                        a[x][y] = a[x][y]*2
                        a[x+1][y] = None
                    if a[x][y] == None:
                        a[x][y] = a[x+1][y]
                        a[x+1][y] = None
    print(a)


a = [[2, None, 2, None],
     [2, None, 2, None],
     [None, None, None, None],
     [None, None, None, None]]

foo(a)
