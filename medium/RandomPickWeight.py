# Given an array w of positive integers, where w[i] describes the weight of index i, write a function
# pickIndex which randomly picks an index in proportion to its weight.

# Note:

# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:

# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# Example 2:

# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
import random


# Preporcessing step - O(NxM)
# pickIndex - O(1)
class Solution:

    def __init__(self, w: 'List[int]'):
        self.w = w
        arr = []
        for i, weight in enumerate(w):
            for _ in range(weight):
                arr.append(i)
        self.arr = arr
        self.n = len(arr)

    def pickIndex(self) -> int:
        randIndex = random.randint(0, self.n - 1)
        return self.arr[randIndex]


# Preporcessing step - O(N)
# pickIndex - O(LogN)
class Solution2:

    def __init__(self, w: 'List[int]'):
        self.w = w
        self.n = len(w)
        self.total = sum(w)
        for i in range(1, self.n):
            w[i] += w[i - 1]

    def pickIndex(self) -> int:
        randIndex = random.randint(1, self.total)

        l, r = 0, self.n - 1
        while l < r:
            mid = (l + r) // 2
            if randIndex <= self.w[mid]:
                r = mid
            else:
                l = mid + 1
        return l
