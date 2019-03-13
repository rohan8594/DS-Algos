# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3

# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder(self, root, arr):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        arr = []
        self.inorder(root, arr)
        return arr[k - 1]
