# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true

# Follow up:
# Could you do it in O(n) time and O(1) space?

# NOTE: My solution is with O(n) space. Checkout leetcode discussions
# for solution with O(1) space


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        cur = head

        while cur:
            stack.append(cur)
            cur = cur.next

        cur = head
        while cur:
            if cur.val != stack.pop().val:
                return False
            cur = cur.next

        return True
