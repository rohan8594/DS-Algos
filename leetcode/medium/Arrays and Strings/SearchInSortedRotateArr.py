# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.
# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        if not nums:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        def binSearch(l, r):
            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return - 1

        rotateIndex = self.getRotateIndex(nums, 0, len(nums) - 1)

        if nums[rotateIndex] == target:
            return rotateIndex

        if rotateIndex == 0:
            return binSearch(0, len(nums) - 1)

        if target < nums[0]:
            return binSearch(rotateIndex, len(nums) - 1)

        return binSearch(0, rotateIndex - 1)

    def getRotateIndex(self, nums, l, r):
        if nums[l] < nums[r]:
            return 0

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] > nums[mid + 1]:
                return mid + 1

            if nums[mid] < nums[l]:
                r = mid - 1
            else:
                l = mid + 1
