# CTCI Question 4.12


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def pathsWithSum(self, root, sum):
        path, res = [], []
        self.findPathSum(root, sum, path, res)
        return len(res)

    def findPathSum(self, root, sum, path, res):
        if root:
            if root.val == sum:
                path.append(root.val)
                res.append(path)

            remain = sum - root.val
            self.findPathSum(root.left, remain, path + [root.val], res)
            self.findPathSum(root.right, remain, path + [root.val], res)


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(5)
e = Node(4)
f = Node(6)

a.left, a.right = b, d
b.left = c
d.left, d.right = e, f

print(a.pathsWithSum(a, 6))  # returns 2
