# Given a binary tree, return the inorder traversal of its nodes' values.

# Example:

# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3

# Output: [1,3,2]
# Follow up: Recursive solution is trivial, could you do it iteratively?


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> list:
        res = []
        self.inOrder(root, res)
        return res

    def inOrder(self, root, res):
        if root:
            self.inOrder(root.left, res)
            res.append(root.val)
            self.inOrder(root.right, res)

    # iteratively
    def inorderTraversal_ii(self, root):
        stack, res = [root], []

        while stack:
            node = stack[len(stack) - 1]
            if node:
                stack.append(node.left)
            else:
                stack.pop()
                if stack:
                    cur = stack.pop()
                    res.append(cur.val)
                    stack.append(cur.right)
        return res
