class BinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, x):
        self.heap.append(x)
        self.size += 1
        self.siftUp(self.size)

    def siftUp(self, i):
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
        self.siftDown(1)
        return res

    def siftDown(self, i):
        while i * 2 <= self.size:
            mc = self.getMinChild(i)

            if self.heap[i] > self.heap[mc]:
                temp = self.heap[mc]
                self.heap[mc] = self.heap[i]
                self.heap[i] = temp
            i = mc

    def getMinChild(self, i):
        if i * 2 == self.size:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[(i * 2) + 1]:
                return i * 2
            else:
                return (i * 2) + 1
