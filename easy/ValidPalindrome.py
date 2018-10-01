# Given a string, determine if it is a palindrome, considering only 
# alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as 
# valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        reverse_stack = []
        
        for current in s:
            if current.isalnum():
                stack.append(current.lower())
                
        for i in range(len(stack) - 1, -1, -1):
            reverse_stack.append(stack[i])
            
        return stack == reverse_stack