# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'list[list[int]]':
        if not root:
            return []

        res = []
        level, nextLevel = [root], []

        while level:
            temp = [node.val for node in level]
            res.append(temp)

            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            level = nextLevel
            nextLevel = []

        return res
