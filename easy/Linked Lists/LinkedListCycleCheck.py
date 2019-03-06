# Given a singly linked list, write a function which takes in the first node
# in a singly linked list and returns a boolean indicating if the linked list
# contains a "cycle".

# A cycle is when a node's next point actually points back to a previous node
# in the list. This is also sometimes known as a circularly linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        seen = set()
        cur = head

        while cur:
            if cur in seen:
                return True

            seen.add(cur)
            cur = cur.next

        return False
