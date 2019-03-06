# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        if len(nums) <= 1:
            return [nums]

        for i in range(len(nums)):
            curNum = [nums[i]]
            remain = nums[0:i] + nums[(i + 1):]

            for perm in self.permute(remain):
                result.append(curNum + perm)

        return result

    # String Permutations
    def permute_string(self, s):
        result = []

        if len(s) <= 1:
            return s

        for i in range(len(s)):
            curChar = s[i]
            remain = s[0:i] + s[(i + 1):]

            for perm in self.permute_string(remain):
                result.append(curChar + perm)

        return result


obj = Solution()
print(obj.permute([1, 2, 3]))
print(obj.permute_string('abc'))
