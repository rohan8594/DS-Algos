package test;

import java.util.Scanner;

public class FibonacciSearch {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		System.out.println("Enter length of array:");
		int length = scan.nextInt();
		
		int[] arr = new int[length];
		for(int loop=0; loop < length; loop++) {
			arr[loop] = scan.nextInt();
		}
		
		System.out.println("Enter number to search:");
		int searchNo = scan.nextInt();
		
		System.out.println(fibonacciSearch(arr, length, searchNo));
		
		scan.close();
	}
	
	public static int fibonacciSearch(int[] arr, int length, int searchNo) {
		
		int fibNum1 = 0; //1st fibonacci no;
		int fibNum2 = 1; //2nd fibonacci no;
		int fibNumN = fibNum1 + fibNum2; //nth Fibonacci no;
		int offSet = -1;
		
		while(fibNumN < length) {
			fibNum2 = fibNum1;
			fibNum1 = fibNumN;
			fibNumN = fibNum1 + fibNum2;
		}
		
		while(fibNumN > 1) {
			int index = getMinIndex(offSet + fibNum2, length-1);
			
			if(arr[index] < searchNo) {
				fibNumN = fibNum1;
				fibNum1 = fibNum2;
				fibNum2 = fibNumN - fibNum1;
				offSet = index;		
				
			} else if (arr[index] > searchNo) {
				fibNumN = fibNum2;
				fibNum1 = fibNum1 - fibNum2;
				fibNum2 = fibNumN - fibNum1;
				
			} else {
				return index;
			}
			
		}
		
		offSet = offSet+1;
		if(fibNum1 == 1 && arr[offSet] == searchNo) {
			return offSet;
		}
		
		return -1;
	}
	
	public static int getMinIndex(int index,int length) {
		return index <= length ? index : length;
	}

}
