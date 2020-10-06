# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of
# the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

# Note:

# The number of nodes will be between 1 and 100.
# The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
# Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
# You must return the copy of the given node as a reference to the cloned graph.
import collections


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        nodeCopy = Node(node.val, [])
        nodeMap = {node: nodeCopy}

        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in nodeMap:
                    neighborCopy = Node(neighbor.val, [])
                    nodeMap[neighbor] = neighborCopy
                    nodeMap[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    nodeMap[node].neighbors.append(nodeMap[neighbor])

        return nodeCopy
