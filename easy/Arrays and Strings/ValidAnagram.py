# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false


class IsAnagram:
    def isAnagram(self, s1, s2):

        self.s1 = s1.replace(' ', '').lower()
        self.s2 = s2.replace(' ', '').lower()

        if (len(s1) != len(s2)):
            return False

        charCount = {}

        for curr in s1:
            if curr not in charCount:
                charCount[curr] = 1
            else:
                charCount[curr] += 1

        for curr in s2:
            if curr in charCount:
                charCount[curr] -= 1
            else:
                charCount[curr] = 1

        for curr in charCount:
            if (charCount[curr] != 0):
                return False

        return True
