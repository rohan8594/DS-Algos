#LeetCode problem link: https://leetcode.com/problems/minimum-operations-to-make-array-equal/

class Solution:
    def minOperations(self, n: int) -> int:
        arr =[]
        num_of_steps =0
        for i in range(n):
            arr.append(2*i+1)
        equall_ele = (arr[0] + arr[n-1])/2
        for j in range(int(n/2)):
            diff = int(abs(arr[j]-equall_ele))
            num_of_steps += diff
        return num_of_steps
