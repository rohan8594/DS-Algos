# Given an integer array nums, find the contiguous subarray within an array (containing
# at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution:
    def maxProduct(self, nums: 'list[int]') -> int:
        maxp, minp = nums[0], nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            tempmax = maxp
            tempmin = minp
            maxp = max(nums[i], max(tempmax * nums[i], tempmin * nums[i]))
            minp = min(nums[i], min(tempmax * nums[i], tempmin * nums[i]))
            res = max(res, maxp)
        return res
