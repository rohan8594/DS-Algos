# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# Backtracking - Problem solving approach that incrementally builds candidates to the solution, and
#                abandons a candidate ("backtracks") as soon as it fails some constraint. It takes a
#                complex problem with a wide decision space and narrows it down to the choices we make at
#                each stack frame of our recurssion.


class Solution:
    def generateParenthesis(self, n: int) -> 'list[str]':
        res = []

        self.generate('', n, n, res)
        return res

    def generate(self, p, left, right, res):
        if left:
            self.generate(p + '(', left - 1, right, res)
        if right > left:  # can only close a bracket that has been opened, hence right > left constraint
            self.generate(p + ')', left, right - 1, res)
        if not right:
            res.append(p)
