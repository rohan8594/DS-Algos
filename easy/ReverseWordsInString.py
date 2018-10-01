# Given a string, you need to reverse the order of characters 
# in each word within a sentence while still preserving whitespace 
# and initial word order.

# Example 1:

# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# Note: In the string, each word is separated by single space and 
# there will not be any extra space in the string.

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        
        for curr in s.split():
            rev = self.reverseStr(curr)
            result.append(rev)
        
        return " ".join(result)
    
    def reverseStr(self, s):
        stack = list(s) # for curr in s: stack.append(curr) 
        reverse_stack = []
        
        for i in range(len(stack)):
            reverse_stack.append(stack.pop())
        
        return "".join(reverse_stack)