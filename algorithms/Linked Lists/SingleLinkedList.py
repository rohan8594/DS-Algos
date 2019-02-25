class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # List traversal
    def printList(self):
        cur = self.head

        while cur:
            print(cur.value)
            cur = cur.next

    # Reverse List
    def reverse(self):
        cur = self.head
        next = None
        prev = None

        while cur:
            next = cur.next
            cur.next = prev

            prev = cur
            cur = next
        self.head = prev

    # Inserting at the beginning of the List
    def insertAtBeginning(self, node):
        node.next = self.head
        self.head = node

    # Inserting at the end of the List
    def insertAtEnd(self, node):
        if self.head is None:
            self.head = node
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    # Inserting in between two Nodes
    def insertInBetween(self, middleNode, newNode):
        newNode.next = middleNode.next
        middleNode.next = newNode

    # Removing an Item from a List
    def removeNode(self, removeKey):
        cur = self.head

        if cur is not None:
            if cur.value == removeKey:
                self.head = cur.next
                return

        while cur is not None:
            if cur.value == removeKey:
                break
            prev = cur
            cur = cur.next

        if cur is None:
            return

        prev.next = cur.next


list = LinkedList()
list.head = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.head.next = e2

# Link second Node to third node
e2.next = e3

e4 = Node("Sun")

# list.printList()
# list.reverse()
list.insertAtEnd(e4)

e5 = Node("Thu")
list.insertInBetween(e3, e5)
list.printList()
print("")
list.removeNode("Thu")
list.printList()
