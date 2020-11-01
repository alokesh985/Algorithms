def MergeSort(arr, left, right):
    if(left < right):

        mid = (left + right) // 2

        MergeSort(arr, left, mid)
        MergeSort(arr, mid + 1, right)
        Merge(arr, left, mid, right)

def Merge(arr, left, mid, right):
    aux = [0] * (right + 1)

    i, j, k = left, mid + 1, left

    while(i <= mid and j <= right):
        if(arr[i] <= arr[j]):
            aux[k] = arr[i]
            i += 1
            k += 1

        else:
            aux[k] = arr[j]
            j += 1
            k += 1

    while(i <= mid):
        aux[k] = arr[i]
        i += 1
        k += 1

    while(j <= right):
        aux[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = aux[i]

def main():
    ip = list(map(int, input("Enter Input Array: ").split()))

    MergeSort(ip, 0, len(ip) - 1)

    print("The Sorted Elements are: ", end = "")
    print(*ip)

if __name__ == "__main__":
    main()