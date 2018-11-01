# There is a robot starting at position (0, 0), the origin, on a 2D plane. 
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after 
# it completes its moves.

# The move sequence is represented by a string, and the character moves[i] 
# represents its ith move. Valid moves are R (right), L (left), U (up), and D 
# (down). If the robot returns to the origin after it finishes all of its moves, 
# return true. Otherwise, return false.

# Note: The way that the robot is "facing" is irrelevant. "R" will always make 
# the robot move to the right once, "L" will always make it move left, etc. Also, 
# assume that the magnitude of the robot's movement is the same for each move.

# Example 1:

# Input: "UD"
# Output: true  

# Example 2:

# Input: "LL"
# Output: false

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        i, j = 0, 0
        
        for cur in moves:
            if cur == 'R':
                j += 1
            if cur == 'L':
                j -= 1
            if cur == 'U':
                i -= 1
            if cur == 'D':
                i += 1
        
        return (0, 0) == (i, j)