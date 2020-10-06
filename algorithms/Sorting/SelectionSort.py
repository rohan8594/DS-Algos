import sys 
A = []
n = int(input("Input Array Size in integer: "));
for i in range(0, n):
 	A.append(input()); 


for i in range(len(A)): 
    min = i 
    for j in range(i+1, len(A)): 
        if A[min] > A[j]: 
            min = j          
    A[i], A[min] = A[min], A[i] 

print ("Sorted array") 
for i in range(len(A)): 
    print(A[i])
