# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Example 1:

# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# Example 2:

# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        if k == 0:
            return head

        tail = None
        cur = head
        listLen = 1

        while cur.next:
            listLen += 1
            cur = cur.next
        tail = cur

        prev, cur = None, head
        if k > listLen:
            k = k % listLen  # if k = 4 and len = 3, rotate by 1
        i = listLen - k

        if listLen == 1 or i == listLen or i == 0:  # edge cases
            return head

        for _ in range(i):
            prev = cur
            cur = cur.next

        if prev:
            prev.next = None
        tail.next = head
        head = cur

        return head
