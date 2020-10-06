# You are given a license key represented as a string S
# which consists only alphanumeric character and dashes.
# The string is separated into N+1 groups by N dashes.

# Given a number K, we would want to reformat the strings
# such that each group contains exactly K characters, except
# for the first group which could be shorter than K, but still
# must contain at least one character. Furthermore, there must
# be a dash inserted between two groups and all lowercase
# letters should be converted to uppercase.

# Given a non-empty string S and a number K, format the string
# according to the rules described above.

# Example 1:
# Input: S = "5F3Z-2e-9-w", K = 4
# Output: "5F3Z-2E9W"

# Example 2:
# Input: S = "2-5g-3-J", K = 2
# Output: "2-5G-3J"


class Solution:
    def licenseKeyFormatting(self, S: 'str', K: 'int') -> 'str':
        result = ''
        count = 0

        for i in range(len(S) - 1, -1, -1):
            if S[i] == '-':
                continue

            if count == K:
                result += '-'
                count = 0

            result += S[i]
            count += 1

        return result[::-1].upper()
