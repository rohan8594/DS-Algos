# Given a non-empty array of digits representing a non-negative 
# integer, plus one to the integer.

# The digits are stored such that the most significant digit is 
# at the head of the list, and each element in the array contain 
# a single digit.

# You may assume the integer does not contain any leading zero, 
# except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [9,9,9]
# Output: [1,0,0,0]
# Explanation: The array represents the integer 999.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        resultArr = []
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        
        result = int(''.join(digits)) + 1
        
        for cur in str(result):
            resultArr.append(int(cur))
            
        return resultArr