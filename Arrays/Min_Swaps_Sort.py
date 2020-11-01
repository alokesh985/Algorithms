# Minimum number of swaps to sort an array

def minimumSwaps(arr):
    # sorted_arr = sorted(arr)
    swaps = 0

    d = {}

    for i in range(len(arr)):
        d[arr[i]] = i

    
    for i in range(len(arr)):
        if(arr[i] == i + 1):
            continue
        
        else:
        
            j = d[i+1]
            arr[i], arr[j] = arr[j], arr[i]
            d[i+1] = i
            d[arr[j]] = j
            swaps += 1  
            
    return swaps


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)

