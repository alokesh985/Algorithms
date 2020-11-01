# This program will give the maximum possible sum of a subarray of size 'k' of a larger array
# Using sliding window technique

def maxSum(arr, k):
    windowSum, maxSum = 0, 0

    # Calculate initial window sum
    for i in range(k):
        windowSum += arr[i]

    # end marks end of the window. The element right after the window ends is the 'end' variable
    for end in range(k, len(arr)):
        windowSum += arr[end] - arr[end - k]

        if(windowSum > maxSum):
            maxSum = windowSum

    return maxSum
    

def main():
    arr = list(map(int, input("Enter array: ").split()))
    k = int(input("Enter subarray size: "))

    print(f"Max sum of subarray of size {k}: {maxSum(arr, k)}")

if __name__ == "__main__":
    main()