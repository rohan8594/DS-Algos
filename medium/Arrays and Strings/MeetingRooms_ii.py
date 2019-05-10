# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si <
# ei), find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1

# Time Complexity: O(NlogN)
# Space Complexity: O(N)
import heapq


class Solution:
    def minMeetingRooms(self, intervals: 'list[list[int]]') -> int:
        if not intervals:
            return 0

        intervals.sort()
        occupiedRooms = [intervals[0][1]]

        for interval in intervals[1:]:
            if occupiedRooms[0] <= interval[0]:
                heapq.heappop(occupiedRooms)

            heapq.heappush(occupiedRooms, interval[1])

        return len(occupiedRooms)
