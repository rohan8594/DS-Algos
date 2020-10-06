# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Note:

# Your algorithm should run in O(n) time and uses constant extra space.

# NOTE: My soln uses O(n) space. Refer to leetcode soln to see soln in O(1) space


class Solution:
    def firstMissingPositive(self, nums: 'list[int]') -> int:
        count = {}

        if 1 not in nums:
            return 1

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] > len(nums):
                nums[i] = 1

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for i in range(1, len(nums) + 2):
            if i not in count:
                return i
