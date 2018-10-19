# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store 
# integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 
# 0 when the reversed integer overflows.

# NOTE: 
# Checkout Leetcode solution for a more optimal approach

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        stack = []
        reverse = []
        result = 0
        
        for cur in str(x):
            if cur == "-":
                negative = True
                continue
            stack.append(cur)
        
        for i in range(len(stack)):
            reverse.append(stack.pop())
            
        if negative:
            result = int("-" + "".join(reverse))
            
        else:
            result = int("".join(reverse))
        
        if result < (-2 ** 31) or result > ((2 ** 31) - 1): # if result is overflowing
            return 0
        
        return result