def pattern_search(n, pattern):

    for i in range(len(n)):
        slider = 0

        if(n[i] == pattern[slider]):
            while(slider < len(pattern)):
                if(n[i + slider] == pattern[slider]):
                    slider += 1
                    continue
                else:
                    break

                slider += 1

            if(slider == len(pattern)):
                print(f"Pattern found at index: {i}")
                exit()
    
    print("Pattern Not Found")

n = input("Enter String: ")
pattern = input("Enter Pattern: ")

op = pattern_search(n, pattern)