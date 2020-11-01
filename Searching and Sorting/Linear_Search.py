# O(n)

def LinearSearch(arr, key):
    for i in range(len(arr)):
        if(key == arr[i]):
            return i

    return -1

def main():
    ip = list(map(int, input("Enter input array: ").split()))
    key = int(input("Enter key to find: "))

    ans = LinearSearch(ip, key)

    if(ans == -1):
        print("Element not found in the list.")

    else:
        print(f"The element is found at index {ans}")

if __name__ == "__main__":
    main()