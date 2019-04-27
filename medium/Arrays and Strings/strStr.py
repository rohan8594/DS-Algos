# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent
# to C's strstr() and Java's indexOf().


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) < 1:
            return 0
        i = 0
        found = False

        for index in range(len(haystack) - len(needle) + 1):
            if needle[i] == haystack[index]:
                j = index
                found = True

                while i < len(needle) and j < len(haystack):
                    if needle[i] != haystack[j]:
                        found = False
                        break
                    i += 1
                    j += 1
                if i < len(needle):
                    found = False
                if not found:
                    i = 0
                else:
                    break

        if not found:
            return -1
        return index

    # More elegant soln.
    def strStr_ii(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1
