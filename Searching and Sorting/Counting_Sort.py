def CountingSort(arr):
    count = [0] * (max(arr)+1)
    
    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # for i in range(len(count)):
    #     count[i] -= 1

    ans = [0] * len(arr)

    # print(count)

    for i in range(len(arr)):
        ans[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return ans

    


def main():
    ip = list(map(int, input("Enter input array: ").split()))
    sorted_arr = CountingSort(ip)
    print("Sorted Array Is: ",end = "")
    print(*sorted_arr)

if __name__ == "__main__":
    main()