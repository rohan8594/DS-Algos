# Given an array of size n, find the majority element. 
# The majority element is the element that appears more 
# than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority 
# element always exist in the array.

# Example 1:

# Input: [3,2,3]
# Output: 3
# Example 2:

# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        
        for cur in nums:
            if cur in counts:
                counts[cur] += 1
            
            else:
                counts[cur] = 1
        
        for cur in counts: break
        max_ele = cur
        
        for cur in list(counts.keys())[1:]:
            if counts[cur] > counts[max_ele]:
                max_ele = cur
        
        return max_ele
