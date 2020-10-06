# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# NOTE: Check out leetcode soln also


class Solution:
    def countPrimes(self, n: 'int') -> 'int':
        count = 0

        for num in range(2, n):
            if self.isPrime(num):
                count += 1
        return count

    def isPrime(self, num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
