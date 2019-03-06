# Write a function that takes a string as input and returns the string reversed.

# Example 1:

# Input: "hello"
# Output: "olleh"
# Example 2:

# Input: "A man, a plan, a canal: Panama"
# Output: "amanaP :lanac a ,nalp a ,nam A"


class ReverseString:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        result = []

        for curr in s:
            stack.append(curr)

        for i in range(len(s)):
            result.append(stack.pop())

        return ''.join(result)
