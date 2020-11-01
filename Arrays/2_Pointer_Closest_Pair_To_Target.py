# This program will find the indices of the pair of elements in an array that are closest to a given target.
# 2 Pointer technique

def closest_pair(arr, target):
    ptr1, ptr2 = 0, len(arr) - 1

    
    sum_of_pairs = arr[ptr1] + arr[ptr2]
    best_difference = abs(target - sum_of_pairs)

    for i in range(len(arr) - 2):
        if(sum_of_pairs < target):
            ptr1 += 1

        else:
            ptr2 -= 1

        sum_of_pairs = arr[ptr1] + arr[ptr2]
        current_difference = abs(target - sum_of_pairs)

        if(current_difference < best_difference):
            closest_pair_index1, closest_pair_index2 = ptr1, ptr2
            best_difference = current_difference

    return (closest_pair_index1, closest_pair_index2)

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    target = int(input("Enter the target: "))

    pair = closest_pair(arr, target)

    print(pair)


