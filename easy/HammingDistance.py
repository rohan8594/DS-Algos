# The Hamming distance between two integers is the number of positions at 
# which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.

# Note:
# 0 ≤ x, y < 2^31.

# Example:

# Input: x = 1, y = 4

# Output: 2

# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑

# The above arrows point to positions where the corresponding bits are different.

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x_in_bin = "{0:032b}".format(x)
        y_in_bin = "{0:032b}".format(y)
        count = 0
        
        for i in range(len(x_in_bin)):
            if x_in_bin[i] != y_in_bin[i]:
                count += 1
        
        return count
