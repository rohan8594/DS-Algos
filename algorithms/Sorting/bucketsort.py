# for float values only

def sort(arr):
    l = len(arr)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp

def BucketSort(arr, no):
    bucket = []
    new_arr = []
    for i in range(10):
        bucket.append([])
    for i in arr: # Add elements to the respective buckets
        bucket[int(i * 10)].append(i) 
    for i in range(10):
        if len(bucket[i]) > 1:
            sort(bucket[i]) # Sorts items in the buckets
            for b in bucket[i]:
                new_arr.append(b)    
        elif len(bucket[i]) == 1:
            new_arr.append(bucket[i][0])
    return new_arr


def display(arr):
    for i in arr:
        print(i , end = ", ")


no = int(input("Enter no of elements:"))
arr = []
sorted_arr = []
for i in range(no):
    temp = float(input())
    arr.append(temp)
sorted_arr = BucketSort(arr, no)
print("Sorted array is:", end = " ")
display(sorted_arr)