# CTCI Question 3.1


class ThreeStacksSingleArray:

    def __init__(self, stackSize=100, numOfStacks=3):
        self.stackSize = stackSize
        self.numOfStacks = numOfStacks
        self.stack = [None] * numOfStacks * stackSize
        self.pointer = [-1] * numOfStacks

    def isEmpty(self, stackNum):
        return self.pointer[stackNum] == -1

    def stackTopIndex(self, stackNum):
        return self.stackSize * stackNum + self.pointer[stackNum]

    def push(self, stackNum, item):
        if self.pointer[stackNum] + 1 >= self.stackSize:
            print('Stack overflow')
        else:
            self.pointer[stackNum] += 1
            self.stack[self.stackTopIndex(stackNum)] = item

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return 'Stack is Empty'
        else:
            item = self.stack[self.stackTopIndex(stackNum)]
            self.stack[self.stackTopIndex(stackNum)] = None
            self.pointer[stackNum] -= 1
            return item

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            print('Stack is Empty')
        else:
            return self.stack[self.stackTopIndex(stackNum)]


# -----------------test-----------------
if __name__ == "__main__":
    array = ThreeStacksSingleArray()
    array.push(2, 11)
    array.push(2, 13)
    print array.pop(0)  # Trying to pop an empty stack.
    print array.peek(2)  # 13
    array.push(0, 20)
    array.push(0, 30)
    print array.pop(0)  # 30
    print array.peek(0)  # 20
