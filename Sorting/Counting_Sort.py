def countingSort(arr):
    # Initilaizing count and output arrays
    count = [0] * (max(arr) + 1)
    op = [0] * len(arr)

    # Counting numbers in indices
    for i in range(len(arr)):
        count[arr[i]] += 1

    # Cumulative addition
    for i in range(1,len(count)):
        count[i] += count[i-1]

    # Putting count in correct position and then decrementing count
    for i in range(len(arr)):
        op[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return op
