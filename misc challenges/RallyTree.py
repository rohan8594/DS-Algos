class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def printTree(self, node):
        cur, next = [], []
        cur.append(node)

        while cur != []:
            temp = []
            for curNode in cur:
                temp.append(curNode.value)
            print(''.join(temp))

            for curNode in cur:
                if curNode.left != None:
                    next.append(curNode.left)
                if curNode.right != None:
                    next.append(curNode.right)

            cur = next
            next = []


a = Node("a")
b = Node("b")
c = Node("c")
x = Node("x")
y = Node("y")
z = Node("z")


a.left = b
a.right = c

b.left = x
b.right = y

c.right = z

a.printTree(a)
