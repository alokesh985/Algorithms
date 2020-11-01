def create_lsp(pattern):
    lsp = [0] * len(pattern)
    i, j = 0, 1

    while(i < len(pattern)):
        if(pattern[i] == pattern[j]):
            lsp[j] = i + 1
            i += 1
            j += 1

        else:
            if(i != 0):
                i = lsp[i - 1]
            
            else:
                lsp[j] = 0
                i += 1

    return lsp

# lsp: longest same prefix
def KMP(string, pattern):
    occurences = []
    lsp = create_lsp(pattern)

    i, j = 0, 0

    while(i < len(string)):
        if(string[i] == pattern[j]):
            i += 1
            j += 1
        
        else:
            if(j != 0):
                j = lsp[j - 1]
            else:
                i += 1

        if(j == len(pattern)):
            occurences.append(i - len(pattern))
            j = 0

    return occurences
        



string = input("Enter Input String: ")
pattern = input("Enter Pattern: ")

occurences = KMP(string, pattern)

if(len(occurences) == 0):
    print("Pattern not found in string.")

for index in occurences:
    print(f"Pattern found at index {index}")