class BinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.moveUp(self.size)

    def moveUp(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                temp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap = temp
            i = i // 2

    def delMin(self):
        res = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.moveDown(1)
        return res

    def moveDown(self, i):
        pass
