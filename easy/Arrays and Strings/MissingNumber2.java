/*

Consider an array of non-negative integers. A second array is formed by shuffling the 
elements of the first array and deleting a random element. Given these two arrays, find 
which element is missing in the second array.

Here is an example input, the first array is shuffled and the number 5 is removed to 
construct the second array.

Input:  MissingNumber2([1,2,3,4,5,6,7],[3,7,2,1,4,6])

Output: 5 is the missing number

*/

class MissingNumber2 {
    public int missingNumber2(int[] arr1, int[] arr2) {

        int result = 0;

        for (int curr : arr1) {
            result ^= curr;
        }

        for (int curr : arr2) {
            result ^= curr;
        }

        return result;
    }

}