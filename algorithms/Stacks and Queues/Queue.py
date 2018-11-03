class Queue:

	def __init__(self):
		self.queue = []

	def isEmpty(self):
		return self.queue == []

	def enqueue(self, item):
		self.queue.insert(0, item)

	def dequeue(self):
		if (self.isEmpty()):
			return None
		else:
			return self.queue.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
print q.dequeue()
print q.isEmpty()