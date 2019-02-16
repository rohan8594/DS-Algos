# CTCI Question 3.6

class AnimalQueue:

	def __init__(self):
		self.dog = []
		self.cat = []
		self.timestamp = 0


	def enqueue(self, animal_type, animal_name):
		if animal_type == 'cat':
			self.cat.insert(0, (animal_name, self.timestamp))
			self.timestamp += 1
		elif animal_type == 'dog':
			self.dog.insert(0, (animal_name, self.timestamp))
			self.timestamp += 1


	def dequeueDog(self):
		if self.dog == []:
			return None

		return self.dog.pop()[0]


	def dequeueCat(self):
		if self.cat == []:
			return None

		return self.cat.pop()[0]


	def dequeueAny(self):
		dog = (None, float('inf')) if self.dog == [] else self.dog.pop()
		cat = (None, float('inf')) if self.cat == [] else self.cat.pop()
		
		if dog[1] == -1 and cat[1] == -1:
			return None
		elif dog[1] < cat[1]:
			self.cat.append(cat)
			return dog[0]
		else:
			self.dog.append(dog)
			return cat[0]
			


#testing
Q = AnimalQueue()

from random import randrange
test_list = [randrange(7) for x in xrange(20)]
for i, x in enumerate(test_list):
	if x < 4:
		if i%2: 
			animal_type = "cat" 
		else: 
			animal_type = "dog"
		test_list[i] = ("enqueue", Q.enqueue, animal_type, animal_type + "#" + str(i))
	elif x == 4:
		test_list[i] = ("dequeue any", Q.dequeueAny)
	elif x == 5:
		test_list[i] = ("dequeue cat", Q.dequeueCat)
	elif x == 6:
		test_list[i] = ("dequeue dog", Q.dequeueDog)


for operation in test_list:
	if len(operation) == 4:
		print operation[0], operation[2], operation[3]
		operation[1](operation[2], operation[3])
	else:
		print operation[0],
		print operation[1]()
