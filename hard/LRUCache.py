# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
# operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise
#            return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its
#                   capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:
# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def removeNode(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def addNode(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node

        node.prev = p
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        n = self.cache[key]
        self.removeNode(n)
        self.addNode(n)  # move node to tail

        return n.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])

        n = Node(key, value)
        self.addNode(n)
        self.cache[key] = n

        if len(self.cache) > self.capacity:
            n = self.head.next
            self.head.next = n.next
            n.next.prev = self.head
            self.cache.pop(n.key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
