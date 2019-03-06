class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = Node(newNode)
        else:
            temp = Node(newNode)
            temp.left = self.left
            self.left = temp

    def insertRight(self, newNode):
        if self.right == None:
            self.right = Node(newNode)
        else:
            temp = Node(newNode)
            temp.right = self.right
            self.right = temp

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def setRootVal(self, val):
        self.value = val

    def getRootVal(self):
        return self.value

    def preOrder(self):
        print(self.getRootVal())
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()


r = Node('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

print("")
r.preOrder()
