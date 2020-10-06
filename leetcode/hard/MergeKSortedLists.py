# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> ListNode:
        heap = []
        dummyHead = cur = ListNode(0)

        # If two elements have the same val, the next tuple items will be compared. To make sure this runs
        # in Python3, we add a tie-breaker "i" in the heap elements (tuples). This assures that the heapq
        # algo will never compare two variables of type ListNode.
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next

            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))

        return dummyHead.next
