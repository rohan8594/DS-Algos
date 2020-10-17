'''
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y]  
(i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed that
all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of arr equal.
'''


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
