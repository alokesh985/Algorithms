def Selection_Sort(arr):
    for i in range(len(arr) - 1):
        min = i

        for j in range(i + 1, len(arr)):
            if(arr[j] < arr[min]):
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr

def main():
    ip = list(map(int, input("Enter Unsorted Array: ").split()))
    sorted_arr = Selection_Sort(ip)

    print("Sorted Array: ", end = "")
    print(* sorted_arr)

if __name__ == "__main__":
    main()