arr = list(map(int, input("Enter the array: ").split()))

prefix_arr = [0] * len(arr)

prefix_arr[0] = arr[0]

for i in range(1, len(arr)):
    prefix_arr[i] += prefix_arr[i-1] + arr[i]

n_queries = int(input("Enter Number of queries: "))

for i in range(n_queries):
    fro, to = map(int, input("Enter from and to respectively: ").split())

    if(fro == 0):
        print(prefix_arr[to])

    else:
        print(prefix_arr[to] - prefix_arr[fro - 1])

        