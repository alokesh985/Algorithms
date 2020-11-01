""" This program will calculate all combinations of an array such that the sum of each combination
is equal to some target value """

""" Whenever you are asked to find some subsets from a larger superset, always think along the lines of
DFS.

For this problem, we will use DFS """

def main():
    arr_input = list(map(int, input("Enter the input array: ").split()))
    target = int(input("Enter Target value: "))

    comb_sum = calc_combination_sum(arr_input, target)

    print(f"The combinations are: {comb_sum}")

def calc_combination_sum(arr, target):
    if(len(arr) == 0 or arr == False):
        return arr

    combinations = []

    arr.sort()

    temp = []
    # Starting and final index
    toFindCombinations(arr, combinations, target, 0, temp)

    return combinations

def toFindCombinations(arr, ans, target, start, temp):

    if(target == 0):
        ans.append(temp.copy())
        return 

    for i in range(start, len(arr)):
        
        if(i != start and arr[i] == arr[i - 1]):
            continue

        if(arr[i] > target):
            break

        temp.append(arr[i])
        toFindCombinations(arr, ans, target - arr[i], i + 1, temp)
        temp.pop(len(temp) - 1)

    


if __name__ == "__main__":
    main()