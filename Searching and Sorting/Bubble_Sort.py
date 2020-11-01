# O(n^2)

def Bubble(arr):

    swaps = 0

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            
            if(arr[j] >= arr[j+1]):
                swaps += 1
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if(swaps == 0):
            break

    return arr


def main():
    ip = list(map(int, input("Enter the unsorted array: ").split()))

    sorted_arr = Bubble(ip)

    print("Sorted Array: ",end = "")
    print(*sorted_arr)

if __name__ == "__main__":
    main()