# Given a non-empty array of integers, every element appears twice 
# except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you 
# implement it without using extra memory?

# Example 1:

# Input: [4,1,2,1,2]
# Output: 4
#
# NOTE: 
# 
# Soln could be improved by using XOR over array. Time complexity
# stays the same, but space complexity reduces to O(1)

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        
        for current in nums:
            if current in seen:
                seen.remove(current)
            else:
                seen.add(current)
                
        return seen.pop()