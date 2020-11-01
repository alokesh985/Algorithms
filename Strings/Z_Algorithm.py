def create_Z(arr):
    Z_arr = [0] * len(arr)

    l, r = 0, 0

    for k in range(1, len(arr)):
        if(k > r):
            l, r = k, k

            while(r < len(arr) and arr[r] == arr[r - l]):
                r += 1

            Z_arr[k] = r - l
            r -= 1

        else:
            k1 = k - l
            if(Z_arr[k1] < (r - k + 1)):
                Z_arr[k] = Z_arr[k1]

            else:
                l = k
                while(r < len(arr) and arr[r] == arr[r - l]):
                    r += 1

                Z_arr[k] = r - l
                r -= 1

    
    return Z_arr

def Z(string, pattern):
    arr = []

    for char in pattern:
        arr.append(char)

    arr.append("$")

    for char in string:
        arr.append(char)


    Z_array = create_Z(arr)

    occurrences = []
    
    for i in range(len(Z_array)):
        if(Z_array[i] == len(pattern)):
            occurrences.append(i - len(pattern) - 1)
    
    return occurrences



string = input("Enter string: ")
pattern = input("Enter Pattern to search: ")

occurrences = Z(string, pattern)

if(len(occurrences) == 0):
    print("Pattern not found in string.")

else:
    for index in occurrences:
        print(f"Pattern found at index {index} in the string.")