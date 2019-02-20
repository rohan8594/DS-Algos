# Deque - Hybrid linear structure provides all the capabilities of
#         stacks and queues in a single data structure


class Deque:

    def __init__(self):
        self.deque = []

    def isEmpty(self):
        return self.deque == []

    def addFront(self, item):
        self.deque.append(item)

    def addRear(self, item):
        self.deque.insert(0, item)

    def removeFront(self):
        if (self.isEmpty()):
            return None

        return self.deque.pop()

    def removeRear(self):
        if (self.isEmpty()):
            return None

        return self.deque.pop(0)


d = Deque()
d.addFront('hello')
d.addRear('world')
print(d.removeFront() + ' ' + d.removeRear())
print(d.isEmpty())
