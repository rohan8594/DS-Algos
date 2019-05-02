# Given two arrays, write a function to compute their intersection.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]

# Note:

# Each element in the result should appear as many times as it shows
# in both arrays. And the result can be in any order.

# Time - O(m + n)
# Space - O(m + n)


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        seen = {}
        result = []

        for cur in nums1:
            if cur not in seen:
                seen[cur] = 1
            else:
                seen[cur] += 1

        for cur in nums2:
            if cur in seen and seen[cur] != 0:
                result.append(cur)
                seen[cur] -= 1

        return result
