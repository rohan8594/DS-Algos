# Top view of a binary tree is the set of nodes visible when the tree is viewed from the top.
# Given a binary tree, print the top view of it. The output nodes can be printed in any order.
# Expected time complexity is O(n)

#        1
#     /     \
#    2       3
#   /  \    / \
#  4    5  6   7
# Top view of the above binary tree: 4 2 1 3 7

#         1
#       /   \
#     2       3
#       \
#         4
#           \
#             5
#              \
#                6
# Top view of the above binary tree: 2 1 3 6


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def printTopView(self, root):
        if not root:
            return []

        horizontalDist = {0: root.val}
        level = [(root, 0)]

        while level:
            nextLevel = []

            for node, dist in level:
                if node.left:
                    nextLevel.append((node.left, dist - 1))
                    if dist - 1 not in horizontalDist:
                        horizontalDist[dist - 1] = node.left.val
                if node.right:
                    nextLevel.append((node.right, dist + 1))
                    if dist + 1 not in horizontalDist:
                        horizontalDist[dist + 1] = node.right.val
            level = nextLevel

        res = [horizontalDist[key] for key in sorted(horizontalDist.keys())]
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)

print("Following are nodes in top",
      "view of Binary Tree")
print(root.printTopView(root))
