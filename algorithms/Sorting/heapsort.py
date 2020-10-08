def down_adjust(heap, i):
    j = 1
    while(j <= (i / 2)):
        if(((j * 2) <= i) and ((j * 2 + 1) <= i)):
            if(heap[j * 2] > heap[j * 2 + 1]):
                if(heap[j * 2] > heap[j]):
                    temp = heap[j * 2]
                    heap[j * 2] = heap[j]
                    heap[j] = temp
                    j = j * 2
                    continue
            else:
                if(heap[j * 2 + 1] > heap[j]):
                    temp = heap[j * 2 + 1]
                    heap[j * 2 + 1] = heap[j]
                    heap[j] = temp
                    j = j * 2 + 1
                    continue
        if((j * 2) <= i):
            if(heap[j * 2] > heap[j]):
                temp = heap[j * 2]
                heap[j * 2] = heap[j]
                heap[j] = temp
                j = j * 2
                continue  
        j = j * 2
    return heap

def create_heap(arr):
    heap = []
    heap.append(arr[0])
    for i in range(1, arr[0]+1):
        k = i
        heap.append(arr[i])
        while(int(k / 2) >= 1):
            if(heap[k] > heap[int(k / 2)]):
                temp = heap[k]
                heap[k] = heap[int(k / 2)]
                heap[int(k / 2)] = temp
                k = int(k / 2)
            else:
                break
    return heap

def heap_sort(heap):
    k = heap[0]
    while(k >= 1):
        temp = heap[1]
        heap[1] = heap[k]
        heap[k] = temp
        k = k - 1
        print(k)
        print(heap[k+1])
        heap = down_adjust(heap, k)
    return heap

def display(arr):
    for k in range(1,len(arr)):
        print(arr[k] , end = ", ")


no = int(input("Enter no of elements:"))
arr = []
arr.append(no)
sorted_arr = []
for i in range(no):
    temp = input()
    arr.append(temp)
heap = create_heap(arr) 
sorted_arr = heap_sort(heap)
print("Sorted array is:", end = " ")
display(sorted_arr)