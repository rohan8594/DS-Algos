def binary_search(arr,ele):

    first = 0
    last = len(arr) - 1

    found = False

    while first <= last and found == False:

        mid = (first + last) // 2

        if arr[mid] == ele:
            found = True
        else:
            if arr[mid] > ele:
                last = mid - 1
            else:
                first = mid + 1

    return found

print(binary_search([1,2,3,4,5,6,7,8,9,10], 4))