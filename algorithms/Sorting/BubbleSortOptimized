# Improves on the non-optimised version in 2 ways:
# - if within a single pass there is no swap, means array is sorted, hence terminate
# - after each pass, need not consider largest last item since it is already in place

def bubbleSortOptimised(arr):

    passes = len(arr) - 1 # for n items, need n - 1 passes
    swapped = True # not sorted to enter loop initially

    while swapped: # if no swap happens in a pass, array is sorted 

        swapped = False # assume sorted
        i = 0 # array index

        while i < passes:

            if arr[i] > arr[i+1]: # not in order
                arr[i], arr[i+1] = arr[i+1], arr[i] # swap
                swapped = True
            i = i + 1 # next pair
        passes = passes - 1 # next pass, need not consider largest item

    return arr

print(bubbleSortOptimised([1, 6, 4, 5, 2, 1, 7, 3]))
