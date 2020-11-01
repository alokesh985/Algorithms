def Insertion_Sort(arr):

    for i in range(1, len(arr)):

        j = i

        while(j > 0 and (arr[j] < arr[j-1])):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr

def main():
    ip = list(map(int, input("Enter unsorted array: ").split()))

    sorted_arr = Insertion_Sort(ip)

    print("Sorted Array: ",end = "")
    print(*sorted_arr)

if __name__ == "__main__":
    main()