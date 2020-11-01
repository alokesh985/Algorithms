# String permutation in lexicographical order

def calc_permutations(ip):
    count = {}
    for ch in ip:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    keys = sorted(count)

    string = []
    count_list = []
    permutations = []

    for key in keys:
        string.append(key)
        count_list.append(count[key])

    res = [0 for i in range(len(ip))]

    calc_permutations_util(string, count_list, res, permutations, 0) # Start at level 0

    return permutations

def calc_permutations_util(string, count, res, permuatations, level):
    if(level == len(res)):
        permuatations.append(res[:]) # VERY IMPORTANT STEP
        
        return 

    for i in range(len(string)):
        
        if(count[i] == 0):
            continue

        res[level] = string[i]
        count[i] -= 1
        calc_permutations_util(string, count, res, permuatations, level + 1)
        count[i] += 1

def main():
    ip = input("Enter String: ")
    permutations = calc_permutations(ip)
    permutations = list(map(lambda x : "".join(x), permutations))
    print("Permuatations are: ")
    for permutation in permutations:
        print(permutation)
    

if __name__ == "__main__":
    main()