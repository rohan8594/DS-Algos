# Given a non-empty integer array of size n, find the minimum number of moves required to
# make all array elements equal, where a move is incrementing n - 1 elements by 1.

# Example:

# Input:
# [1,2,3]

# Output:
# 3

# Explanation:
# Only three moves are needed (remember each move increments two elements):

# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

# NOTE: Logic explained in leetcode solns.


class Solution:
    # Dynamic Programming
    def minMoves(self, nums: 'list[int]') -> int:
        nums = sorted(nums)
        moves = 0

        for i in range(1, len(nums)):
            diff = moves + (nums[i] - nums[i - 1])
            nums[i] += moves
            moves += diff

        return moves

    # Using Sorting; little more elegant

    # Visualize the nums array as a bar graph where the value at each index is a bar of height nums[i].
    # Sort the array such that the bar at index 0 is minimum height and the bar at index N-1 is highest.

    # Now in the first iteration, make a sequence of moves such that the height at index 0 is equal to
    # height at index N-1. Clearly this takes nums[N-1]-nums[0] moves. After these moves, index N-2 will
    # be the highest and index 0 will still be the minimum and nums[0] will be same as nums[N-1].

    # In the next iteration, lets do nums[N-2]-nums[0] moves. After this iteration, nums[0], nums[N-2],
    # and nums[N-1] will be the same.
    def minMoves2(self, nums: 'list[int]') -> int:
        nums = sorted(nums)
        moves = 0

        for i in range(len(nums) - 1, 0, -1):
            moves += nums[i] - nums[0]

        return moves
