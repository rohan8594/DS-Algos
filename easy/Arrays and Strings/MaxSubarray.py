# Given an integer array nums, find the contiguous subarray (containing
# at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cont_sum = nums[0]
        max_sum = nums[0]

        for curr in nums[1:]:
            cont_sum = max(curr + cont_sum, curr)
            max_sum = max(cont_sum, max_sum)

        return max_sum
