# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.


class Solution:
    def longestCommonPrefix(self, strs: 'list[str]') -> str:
        if not strs:
            return ""

        res = ""
        i = 0
        done = False

        while True:
            try:  # for cases where array index is out of bounds
                curChar = strs[0][i]
                for s in strs[1:]:
                    if s[i] != curChar:
                        done = True
                        break
                if done:
                    break
                else:
                    res += curChar
                    i += 1
            except:
                return res
        return res
