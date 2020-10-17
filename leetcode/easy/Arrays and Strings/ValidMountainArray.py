class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <= 2: return False
        if A[0] > A[1]: return False
        
        inc = True
        for i in range (1, len(A)):
            if (A[i]>A[i-1]):
                if not inc: return False
            elif(A[i]<A[i-1]):
                inc = False
            else:
                return False
        return not inc
    
                