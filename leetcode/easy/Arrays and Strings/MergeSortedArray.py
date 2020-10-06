# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one
# sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n)
# to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        arrIndex = m + n - 1

        while j >= 0 and i >= 0:
            if (nums2[j] > nums1[i]):
                nums1[arrIndex] = nums2[j]
                j -= 1

            else:
                nums1[arrIndex] = nums1[i]
                i -= 1
            arrIndex -= 1

        if j >= 0:
            for k in range(j, -1, -1):
                nums1[arrIndex] = nums2[k]
                arrIndex -= 1

    # Cleaner solution
    def merge2(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
