def QuickSort(arr, l, r):
    if(l < r):

        pivot_index = Partition(arr, l, r)

        # Recursively sorting left and right subarrays

        QuickSort(arr, l, pivot_index - 1)
        QuickSort(arr, pivot_index + 1, r)

def Partition(arr, l, r):
    pivot = arr[l]  # Taking first element as pivot

    i = r + 1

    for j in range(r, l, -1):
        if(arr[j] > pivot):
            i -= 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i - 1], arr[l] = arr[l], arr[i - 1]

    return(i-1)

def main():
    ip = list(map(int, input("Enter Input Array: ").split()))
    QuickSort(ip, 0, len(ip) - 1)
    print("Sorted Array is: ", end = "")
    print(*ip)

if __name__ == "__main__":
    main()