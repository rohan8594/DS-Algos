# CTCI Question 3.5

class Stack:

	def __init__(self):
		self.stack = []


	def __str__(self):
		return self.stack


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
		
		return self.stack[len(self.stack) - 1]


	def sortStack(self):
		temp_stack = Stack()

		while not self.isEmpty():
			temp = self.pop()

			if temp_stack.isEmpty():
				temp_stack.push(temp)
			
			else:
				while temp < temp_stack.peek():
					self.push(temp_stack.pop())
				temp_stack.push(temp)

		return temp_stack



from random import randrange

test_items = [randrange(20) for x in xrange(20)]
print(test_items)

S = Stack()
for item in test_items:
	S.push(item)

result = S.sortStack()
print(result.__str__())