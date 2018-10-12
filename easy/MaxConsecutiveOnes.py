# Given a binary array, find the maximum number of consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s.
#     The maximum number of consecutive 1s is 3.

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        max_sum = 0
        
        for curr in nums:
            if curr == 1:
                curr_sum += 1
            
            else:
                max_sum = max(max_sum, curr_sum)
                curr_sum = 0
        
        return max(max_sum, curr_sum)