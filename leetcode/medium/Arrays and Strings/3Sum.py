# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums: 'list[int]') -> 'list[list[int]]':
        if len(nums) < 3:
            return []

        if nums == [0] * len(nums):
            return [[0, 0, 0]]

        res = set()

        for i in range(len(nums)):
            seen = set()
            remainSum = -nums[i]
            remainNums = nums[:i] + nums[(i + 1):]

            for cur in remainNums:
                remain = remainSum - cur

                if remain not in seen:
                    seen.add(cur)
                else:
                    temp = [nums[i], remain, cur]
                    temp.sort()
                    res.add(tuple(temp))

        return list(res)
