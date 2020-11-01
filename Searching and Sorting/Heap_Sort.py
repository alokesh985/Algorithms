def HeapSort(arr):

    # To initially build a max heap, we will begin calling Heapify method from
    # the last non-leaf node. We will continue calling Heapify till the root node

    # We subtract 1 because of 0-based indexing.
    # Say, we have an array, [10, 17, 20, 1, 5, 10, 15]
    # The last non leaf node is 20.
    # So, len(arr) = 7. Therefore, (len(arr) // 2) - 1 = 2. array[2] = 10.
    n = (len(arr) // 2) - 1

    for i in range(n, -1, -1):
        MaxHeapify(arr, len(arr), i)

    # Swap last element with largest element (i.e., first element (root) of the heap)
    # Do not touch the last element again as it is in the correct position
    
    for i in range(len(arr) - 1, 0, -1): # Till 0 because after n-1 iterations, the array will be sorted

        arr[i], arr[0] = arr[0], arr[i] # After creating the heap, the largest element i.e., root of the heap is at arr[0]
        MaxHeapify(arr, i, 0) # Calling MaxHeapify on root node i.e., arr[0]

    return arr

# 'i' is the node from which we are calling MaxHeapify
def MaxHeapify(arr, n, i): 
    largest = i
    left_child = (2 * i) + 1 # Heap Property
    right_child = (2 * i) + 2

    if(left_child < n and arr[left_child] > arr[largest]): # The pointer should not go out of bounds
        largest = left_child

    if(right_child < n and arr[right_child] > arr[largest]):
        largest = right_child

    if(largest != i): # Root is not the largest, swap is needed
        arr[largest], arr[i] = arr[i], arr[largest]

        MaxHeapify(arr, n, largest) # Recursively calling max heap


def main():
    ip = list(map(int, input("Enter input array: ").split()))
    sorted_arr = HeapSort(ip)
    print("Sorted Array: ",end = "")
    print(*sorted_arr)

if __name__ == "__main__":
    main()