def MergeUtility(arr, sorted_arr, l, r):
    if(l < r):

        mid = (l + r) // 2

        MergeUtility(arr, sorted_arr, l, mid)
        MergeUtility(arr, sorted_arr, mid + 1, r)

        Merge(arr, sorted_arr, l, mid, r)

    

def Merge(arr, sorted_arr, l, mid, r):
    i, j, k = l, mid + 1, l

    while(i <= mid and j <= r):
        if(arr[i] <= arr[j]):
            sorted_arr[k] = arr[i]
            i += 1
            k += 1

        else:
            sorted_arr[k] = arr[j]
            k += 1
            j += 1
    
    while(i <= mid):
        sorted_arr[k] = arr[i]
        k += 1
        i += 1

    while(j <= r):
        sorted_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(l, r + 1):
        arr[i] = sorted_arr[i]

def MergeSort(arr):
    sorted_arr = [0] * len(arr)

    return MergeUtility(arr, sorted_arr, 0, len(arr) - 1)

arr = list(map(int, input("Enter elements of the array: ").split()))

MergeSort(arr)

print("Sorted Array is: ", end = "")
print(*arr)