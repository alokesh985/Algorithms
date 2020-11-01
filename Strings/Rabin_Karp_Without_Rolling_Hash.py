from string import ascii_letters

def calculate_hash(input, hash_table):
    hash = 0
    for i in list(input):
        hash += hash_table[i]

    return hash

def Rabin_Karp(input, pattern):
    n = len(input)
    m = len(pattern)
    hash_table = {i : ord(i) for i in list(ascii_letters)}

    pattern_hash = calculate_hash(pattern, hash_table)

    occurrences = []

    for i in range(n - m + 1):
        temp = input[i : i + m]
        if(calculate_hash(temp, hash_table) == pattern_hash):
            if(temp == pattern):
                occurrences.append(i)

    return occurrences
    
    

string = input("Enter String: ")
pattern = input("Enter Pattern: ")

occurrences = Rabin_Karp(string, pattern)

if(len(occurrences) == 0):
    print("Pattern not found in string")

else:
    for index in occurrences:
        print(f"Pattern found at index {index} of input string.")