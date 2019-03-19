# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Note:

# Each element in the result must be unique.
# The result can be in any order.


class Solution:
    def intersection(self, nums1: 'list[int]', nums2: 'list[int]') -> 'list[int]':
        seen, res = set(), set()

        for cur in nums1:
            if cur not in seen:
                seen.add(cur)

        for cur in nums2:
            if cur in seen:
                res.add(cur)

        return list(res)
