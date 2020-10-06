# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getPathSum(self, root, sum, path, res):
        if root:
            if root.val == sum and not root.left and not root.right:
                path.append(root.val)
                res.append(path)

            remain = sum - root.val
            self.getPathSum(root.left, remain, path + [root.val], res)
            self.getPathSum(root.right, remain, path + [root.val], res)

    def pathSum(self, root: TreeNode, sum: int) -> 'list[list[int]]':
        path, res = [], []
        self.getPathSum(root, sum, path, res)
        return res
