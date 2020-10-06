# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

# NOTE: Logic is explained in leetcode solns.
import heapq


class Solution:
    # O(nlogk) time, O(n) space
    def findKthLargest(self, nums: 'list[int]', k: int) -> int:
        heap = []

        # heapq.heapify(heap) <--- This is much better. Time complexity is O(k); complexity of below
        #                          chunk of code is O(klogk)
        for num in nums[:k]:
            heapq.heappush(heap, num)

        for num in nums[k:]:
            if num > heap[0]:
                # heapq.heappop(heap); heapq.heappush(heap, num)
                heapq.heapreplace(heap, num)
        return heap[0]

    # O(nk) time, O(1) space, bubble sort idea, TLE
    def findKthLargest2(self, nums, k):
        for i in range(k):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[len(nums)-k]
