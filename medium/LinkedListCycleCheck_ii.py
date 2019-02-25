# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# NOTE: This solution has O(n) space complexity. Jose Portilla and leetcode solutions use two pointers
# to solve this in O(1) space. In interview setting, if I give this answer, they may ask to optimize it,
# during which leetcode soln. could be useful.


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        cur = head

        while cur:
            if cur in seen:
                return cur

            seen.add(cur)
            cur = cur.next
        return None
