# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

# NOTE: My soln is in n^2 time. Check out the nlogn soln before interviews


class Solution:
    def lengthOfLIS(self, nums: 'List[int]') -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            maxval = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxval = max(maxval, dp[j])
            dp[i] += maxval
        return max(dp)

    # Returns max subsequence instead of max length
    def lengthOfLIS_ii(self, nums: 'List[int]') -> int:
        if not nums:
            return 0

        dp = {i: [num] for i, num in enumerate(nums)}

        for i in range(1, len(nums)):
            maxval = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    if len(dp[j]) > maxval:
                        maxval = len(dp[j])
                        dp[i] = dp[j] + [nums[i]]
        print(dp)
