# Given a string, find the first non-repeating character in it 
# and return it's index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        unique = {}
        seen = set()
        index = 0
        
        for curr in s:
            if curr not in seen:
                unique[curr] = index
                seen.add(curr)
            else:
                # to avoid KeyError first check if key exists
                # ALT: unique.pop(curr, None)
                if (curr in unique):
                    unique.pop(curr)
            index += 1
        
        if unique == {}:
            return -1
        else:
            lower = unique[list(unique.keys())[0]]
            for curr in unique.keys():
                lower = min(lower, unique[curr])
            return lower