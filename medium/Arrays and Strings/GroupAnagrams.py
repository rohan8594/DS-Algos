# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

# Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs.
# Space Complexity: O(NK), the total information content stored in ans.
import collections


class Solution:
    def groupAnagrams(self, strs: 'list[str]') -> 'list[list[str]]':
        charCounts = collections.defaultdict(list)
        res = []

        for curStr in strs:
            count = [0] * 26
            for char in curStr:
                count[ord(char) - 97] += 1
            count = tuple(count)
            charCounts[count].append(curStr)

        for _, val in charCounts.items():
            res.append(val)
        return res
