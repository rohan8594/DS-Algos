# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
# Note:

# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
import heapq
from collections import Counter
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: 'list[int]', k: int) -> 'list[int]':
        res = []
        heap, count = [], {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for key, val in count.items():
            heap.append((-1 * val, key))

        heapq.heapify(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

    # Alternate soln using bucket sort
    def topKFrequent2(self, nums, k):
        # key=> num, val => count of num
        counter = Counter(nums)
        # key=> count of num, val => list of num with that count
        bucket = defaultdict(list)

        for key, val in counter.items():
            bucket[val].append(key)

        ret = []
        for i in range(len(nums), 0, -1):
            if bucket[i]:
                ret += bucket[i]
            if len(ret) == k:
                return ret
