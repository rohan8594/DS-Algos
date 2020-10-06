# Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove
# all leaves, repeat until the tree is empty.

# Example:
# Input: [1,2,3,4,5]

#           1
#          / \
#         2   3
#        / \
#       4   5

# Output: [[4,5,3],[2],[1]]
import collections


class Solution(object):
    def findLeaves(self, root):
        def dfs(root, dic):
            if not root:
                return 0
            left = dfs(root.left, dic)
            right = dfs(root.right, dic)
            lev = max(left, right) + 1
            dic[lev].append(root.val)
            return lev

        dic, ret = collections.defaultdict(list), []
        dfs(root, dic)
        for i in range(1, len(dic) + 1):
            ret.append(dic[i])
        return ret
