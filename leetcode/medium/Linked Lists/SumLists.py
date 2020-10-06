# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
        i, j = 0, 0

        while l1:
            num1 += l1.val * (10 ** i)
            i += 1
            l1 = l1.next

        while l2:
            num2 += l2.val * (10 ** j)
            j += 1
            l2 = l2.next

        num = num1 + num2
        head = ListNode(num % 10)
        num = num // 10

        cur = head
        while num != 0:
            cur.next = ListNode(num % 10)
            cur = cur.next
            num = num // 10
        return head
