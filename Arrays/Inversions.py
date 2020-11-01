def Inversions(arr, m):
     sorted_arr = [0] * m
     return Inversion_Merge_Sort(arr, sorted_arr, 0, m - 1)

def Inversion_Merge_Sort(arr, sorted_arr, l, r):
    inversions = 0

    if(l < r):
        mid = (l + r) // 2

        inversions += Inversion_Merge_Sort(arr, sorted_arr, l, mid)
        inversions += Inversion_Merge_Sort(arr, sorted_arr, mid+1, r)
        inversions += Merge(arr, sorted_arr, l, mid, r)

    return inversions

def Merge(arr, sorted_arr, l, mid, r):
    i, j, k = l, mid + 1, l

# i points to left sorted subarray, j points to right sorted subarray and k points to sorted_arr

    inversions = 0

    while(i <= mid and j <= r):
        if(arr[i] <= arr[j]):
            sorted_arr[k] = arr[i]
            i += 1
            k += 1
        else:
            sorted_arr[k] = arr[j]

            # If one element in left subarray is an inversion, all elements to right of left subarray will also
            # be and inversion because the left subarray is sorted
            inversions += (mid - i + 1)
            k += 1
            j += 1

    while(i <= mid):
        sorted_arr[k] = arr[i]
        i += 1
        k += 1

    while(j <= r):
        sorted_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(l, r+1):
        arr[i] = sorted_arr[i]

    return inversions

n = int(input())

for i in range(n):
    m = int(input())

    arr = list(map(int, input().split()))

    print(Inversions(arr, m))