# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isMirror(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return False

        return (node1.val == node2.val) and self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)

    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
