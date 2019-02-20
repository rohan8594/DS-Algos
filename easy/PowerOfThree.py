# Given an integer, write a function to determine if it is a power of three.

# Example 1:

# Input: 27
# Output: true
# Example 2:

# Input: 0
# Output: false
# Example 3:

# Input: 9
# Output: true
# Example 4:

# Input: 45
# Output: false

# This solution has O(log(N) base 3) time complexity, but I think
# leetcode solution uses a base conversion trick to solve in O(1) time.


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = 1  # Set to 1 instead of 0, coz we want result == n to give false if n = 0
        count = 0

        while result < n:
            count += 1
            result = 3 ** count

        return result == n
