# Given an array, rotate the array to the right by k steps, where k is
# non-negative.

# Example 1:

# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Note:

# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        stack = []
        finalArr = []

        for i in range(k):
            stack.append(nums.pop())

        for i in range(len(stack)):
            finalArr.append(stack.pop())

        for cur in nums:
            finalArr.append(cur)

        return finalArr

        # Rotate Inplace (space complexity - O(1))
        # Logic is explained in leetcode solns.
    def rotate_inplace(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)  # for edge cases where k > len(nums)
        # without this, we get index out of bound error when k > len(nums)
        j = 0

        for i in range(len(nums) // 2):
            temp = nums[i]
            nums[i] = nums[len(nums) - 1 - i]
            nums[len(nums) - 1 - i] = temp

        for i in range(k // 2):
            temp = nums[i]
            nums[i] = nums[k - 1 - i]
            nums[k - 1 - i] = temp

        for i in range(k, k + ((len(nums) - k) // 2)):
            temp = nums[i]
            nums[i] = nums[len(nums) - 1 - j]
            nums[len(nums) - 1 - j] = temp
            j += 1
