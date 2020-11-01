def calc_permutations(ip, level, res=None):
    ip = list(ip)
    if(res is None):
        res = []
    if(level == len(ip)):
        res.append(ip[:]) # VERY IMPORTANT STEP FOR RECORDING RESULTS OF RECURSION
    else:
        for j in range(level, len(ip)):
            ip[level], ip[j] = ip[j], ip[level]
            calc_permutations(ip, level + 1, res)
            ip[level], ip[j] = ip[j], ip[level]
    return res

def main():
    ip = input("Enter String: ")
    permutations = calc_permutations(ip, 0) # Starting from level 0
    permutations = list(map(lambda x : "".join(x), permutations))
    print("Permuatations are: ")
    for permutation in permutations:
        print(permutation)
    

if __name__ == "__main__":
    main()