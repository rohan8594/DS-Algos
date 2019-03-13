# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie,
# from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

#       1
#      / \
#     2   3
#    /     \
#   4       5


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> 'list[list[int]]':
        if root is None:
            return []

        res = []
        level, nextLevel = [root], []
        depth = 1

        while level:
            if depth % 2 == 0:
                # Reversing step under the hood is O(N), better to loop from end to front to improve complexity in interviews
                temp = [node.val for node in level[::-1]]
            else:
                temp = [node.val for node in level]
            res.append(temp)

            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            level = nextLevel
            nextLevel = []
            depth += 1
        return res
