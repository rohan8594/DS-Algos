# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]


class Solution:
    def generate(self, numRows: int) -> 'list[list[int]]':
        arr, prev = [], []

        for k in range(1, numRows + 1):
            cur = []
            for i in range(k):
                if i == 0 or i == k - 1:
                    cur.append(1)
                else:
                    cur.append(prev[i - 1] + prev[i])
            prev = cur
            arr.append(cur)
        return arr
