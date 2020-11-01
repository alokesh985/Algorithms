# O(log(n))

def BinarySearch(arr, start, end, key):
    
    if(start <= end):

        mid = (start + end) // 2
        
        if(arr[mid] == key):
            return mid

        elif(key < arr[mid]):
            return BinarySearch(arr, start, mid-1, key)

        else:
            return BinarySearch(arr, mid + 1, end, key)

    else:
        return -1

def main():
    ip = list(map(int, input("Enter the sorted input array: ").split()))

    key = int(input("Enter the element to search: "))

    ans = BinarySearch(ip, 0, len(ip) - 1, key)

    if(ans == -1):
        print("Element not found in the list")

    else:
        print(f"Element found at index {ans}")

if __name__ == "__main__":
    main()