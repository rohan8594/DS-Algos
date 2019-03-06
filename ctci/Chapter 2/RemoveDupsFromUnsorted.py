# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        seen = set()
        prev = None
        cur = head

        while cur:
            if cur.val in seen:
                prev.next = cur.next
            else:
                seen.add(cur.val)
                prev = cur

            cur = cur.next
        return head
