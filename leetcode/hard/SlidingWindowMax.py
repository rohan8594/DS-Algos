# Given an array nums, there is a sliding window of size k which is moving from the very left of the
# array to the very right. You can only see the k numbers in the window. Each time the sliding window
# moves right by one position. Return the max sliding window.

# Example:

# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

# Follow up:
# Could you solve it in linear time?

# Note: Use leetcode discussions and youtube for explanation. Basically, this problem uses the concept of
#       a decreasing deque. Front of the deque will always have max element in a window.
import collections


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: int) -> 'List[int]':
        res = []
        deq = collections.deque()

        for i in range(len(nums)):
            if deq and deq[0] < (i + 1) - k:
                deq.popleft()

            while deq:
                if nums[i] > nums[deq[-1]]:
                    deq.pop()
                else:
                    break
            deq.append(i)

            if i >= k - 1:
                res.append(nums[deq[0]])
        return res
