class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None

        # When node.val > R, we know that the trimmed binary tree must occur to the left of the node
        if root.val < L:
            return self.trimBST(root.right, L, R)

        # when node.val < L, the trimmed binary tree occurs to the right of the node
        elif root.val > R:
            return self.trimBST(root.left, L, R)

        # Otherwise, we will trim both sides of the tree
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
