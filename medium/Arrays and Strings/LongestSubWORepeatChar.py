# Given a string, find the length of the longest substring without repeating characters.

# Example 1:

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    # Naive approach
    def lengthOfLongestSubstring_naive(self, s: str) -> int:
        maxLen = 0

        for i in range(len(s)):
            seen = set()
            curLen = 0
            for j in range(i, len(s)):
                if s[j] not in seen:
                    curLen += 1
                    seen.add(s[j])
                    maxLen = max(maxLen, curLen)
                else:
                    break
        return maxLen

    # Similar logic, but now uses max sliding window concept to do it inside one loop
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, maxLen = 0, 0, 0
        seen = set()

        while i < len(s) and j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                maxLen = max(maxLen, j - i)
            else:
                seen.remove(s[i])
                i += 1
        return maxLen
