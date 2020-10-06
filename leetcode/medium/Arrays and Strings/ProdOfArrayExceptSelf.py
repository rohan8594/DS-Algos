# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to
# the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for
# the purpose of space complexity analysis.)

# LOGIC: The idea is simply. The product basically is calculated using the numbers before the current
#        number and the numbers after the current number. Thus, we can scan the array twice. First, we
#        calcuate the running product of the part before the current number. Second, we calculate the
#        running product of the part after the current number through scanning from the end of the array.


class Solution:
    def productExceptSelf(self, nums):
        x, y = 1, 1
        output = []

        for i in range(len(nums)):
            output.append(x)
            x = x * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * y
            y = y * nums[i]

        return output
