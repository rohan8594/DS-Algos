# Given a string, find the first non-repeating character in it
# and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.


class Solution:
    def firstUniqChar(self, s: 'str') -> 'int':
        charCounts = {}

        for cur in s:
            if cur not in charCounts:
                charCounts[cur] = 1
            else:
                charCounts[cur] += 1

        for i in range(len(s)):
            if charCounts[s[i]] == 1:
                return i
        return -1
