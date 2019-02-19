def bubbleSort(arr):

    for i in range(len(arr) - 1, 0, -1):

        for k in range(i):
            if arr[k] > arr[k + 1]:
                arr[k], arr[k + 1] = arr[k + 1], arr[k]

    return arr


print(bubbleSort([1, 6, 4, 5, 2, 1, 7, 3]))
