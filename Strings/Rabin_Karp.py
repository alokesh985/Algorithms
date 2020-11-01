def Rabin_Karp(text, pattern, prime = 101):
    
    pattern_hash = calc_hash(pattern, len(pattern) - 1)
    text_hash = calc_hash(text, len(pattern) - 1)

    occurences = []

    for i in range(1, len(text) - len(pattern) + 2):
        if (pattern_hash == text_hash):
            if equal(text[i - 1 : i + len(pattern) - 1], pattern) is True:
                occurences.append(i - 1)
        if(i < len(text) - len(pattern) + 1):    
            text_hash = rolling_hash(text, i-1, i + len(pattern) - 1, text_hash, len(pattern))
    return occurences
    
def equal(str1, str2):
    if str1 != str1:
        return False
    else:
        return True
    
def calc_hash(input, end, prime = 101):
    hash = 0
    for i in range(end + 1):
        hash = hash + ord(input[i]) * pow(prime, i)
    return hash

def rolling_hash(input, old_index, new_index, old_hash, pattern_len, prime = 101):
    new_hash = old_hash - ord(input[old_index])
    new_hash /= prime
    new_hash += ord(input[new_index]) * pow(prime, pattern_len - 1)
    return new_hash

def main():
    text = input("Enter Text: ")
    pattern = input("Enter pattern: ")
    occurences = Rabin_Karp(text, pattern)
    print("Pattern Occurs at Indices: ", end = "")
    print(*occurences, sep = ", ")

if __name__ == "__main__":
    main()