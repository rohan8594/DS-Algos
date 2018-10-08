/*
Implement function ToLowerCase() that has a string parameter str, 
and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"
*/

class Solution {
    public String toLowerCase(String str) {
        char[] A = str.toCharArray();
        
        for (int i = 0; i < A.length; i++) {
            if (A[i] >= 'A' && A[i] <= 'Z') {
                A[i] = (char)(A[i] - 'A' + 'a'); // or (A[i] + 32)
            }
        }
        return new String(A);
    }
}