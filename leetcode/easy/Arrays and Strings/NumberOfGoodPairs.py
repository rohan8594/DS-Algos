#Given an array of integers nums.
#
#A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#
#Return the number of good pairs.

#Input: nums = [1,2,3,1,1,3]
#Output: 4
#Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1
        return cnt
