# class node to store data and next
class Node:

  def __init__(self,data, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev
  
  # defining getter and setter for data, next and prev
  def getData(self):
    return self.data
  
  def setData(self, data):
    self.data = data
  
  def getNextNode(self):
    return self.next
  
  def setNextNode(self, node):
    self.next = node
    
  def getPrevNode(self):
    return self.prev
  
  def setPrevNode(self, node):
    self.prev = node

# class Linked List
class LinkedList:

  def __init__(self, head=None):
    self.head = head
    self.size = 0

  def getSize(self):
    return self.size

  def addNode(self, data):
    node = Node(data, None, self.head)
    self.head = node
    # incrementing the size of the linked list
    self.size += 1
    return True
  
  # delete a node from linked list
  def removeNode(self, value):
    prev = None
    curr = self.head
    while curr:
      if curr.getData() == value:
        if prev:
            prev.setNextNode(curr.getNextNode())
        else:
            self.head = curr.getNextNode()
        return True
        
      prev = curr
      curr = curr.getNextNode()
        
    return False
  
  # find a node in the linked list
  def findNode(self,value):
    curr = self.head
    while curr:
      if curr.getData() == value:
        return True
      else:
        curr = curr.getNextNode()
    return False
  
  # print the linked list
  def printLL(self):
    curr = self.head
    while curr:
      print(curr.data)
      curr = curr.getNextNode()
      
           
myList = LinkedList()
print("Inserting")
print(myList.addNode(5))
print(myList.addNode(15))
print(myList.addNode(25))

myList.printLL()

print(myList.getSize())

print(myList.findNode(25))

print(myList.removeNode(25))

myList.printLL()