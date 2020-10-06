# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# Example:

# root = [5,3,6,2,4,null,7]
# key = 3

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Given key to delete is 3. So we find the node with value 3 and delete it.

# One valid answer is [5,4,6,2,null,null,7].
# Another valid answer is [5,2,6,null,4,null,7], shown in the following BST.

#     5
#    / \
#   2   6
#    \   \
#     4   7

# NOTE: Only 48 / 85 test cases passing. Check leetcode or J Portilla's soln for correct soln.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val == key:
            temp = root.right
            root = root.left
            if root:
                if root.right:
                    root.right.right = temp
                else:
                    root.right = temp
            return root

        node = root

        while node:
            prev = node
            if node.val > key:
                node = node.left
            elif node.val < key:
                node = node.right

            if not node:
                continue

            if node.val == key:
                temp = node.right
                node = node.left
                if prev.left:
                    if prev.left.val == key:
                        prev.left = node
                elif prev.right:
                    if prev.right.val == key:
                        prev.right = node
                if node:
                    if node.right:
                        node.right.right = temp
                    else:
                        node.right = temp
                break
        return root
