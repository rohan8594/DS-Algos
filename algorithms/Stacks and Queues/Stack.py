class Stack:

	def __init__(self):
		self.stack = []


	def isEmpty(self):
		return self.stack == []


	def push(self, item):
		self.stack.append(item)


	def pop(self):
		if (self.isEmpty()):
			return None
		
		return self.stack.pop()


	def peek(self):
		if (self.isEmpty()):
			return None
		
		return self.stack[len(self.stack)  - 1]



s = Stack()
print s.isEmpty()
s.push(1)
s.push('two')
print s.peek()
s.push(True)
print s.isEmpty()
print s.pop()
print s.pop()
print s.pop()
print s.isEmpty()
print s.pop()