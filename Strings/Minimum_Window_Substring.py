""" This program finds the minimum length of the substring in a string such that the substring
contains all the characters of the pattern """
def MinWindowSub(string, pattern):
    len_pattern = len(pattern)
    len_string = len(string)

    if(len_pattern > len_string):
        return 0

    hash_pattern = [0] * 256 # 256 is the number of characters in ASCII table
    hash_string = [0] * 256

    # Store occurrence of characters in pattern
    for i in range(len_pattern):
        hash_pattern[ord(pattern[i])] += 1

    lptr, start_index, minLen = 0, -1, float('inf') # start_index is starting index of the window


    count = 0 # count of characters in pattern

    for i in range(len_string):
        hash_string[ord(string[i])] += 1

        if(hash_pattern[ord(string[i])] != 0 and hash_string[ord(string[i])] <= hash_pattern[ord(pattern[i])]):

            count += 1

        if count == len_pattern: # If all characters have been matched
            
            # Incrementing lptr to reduce size of window by checking 2 conditions:
            # 1. Character does not occur in pattern
            # 2. Character occurs more times than it does in pattern
            while(hash_string[ord(string[lptr])] > hash_pattern[ord(string[lptr])] or hash_pattern[ord(string[lptr])] == 0):

                if(hash_string[ord(string[lptr])] > hash_pattern[ord(string[lptr])]):
                    hash_string[ord(string[lptr])] -= 1

                lptr += 1       

            # Update Window size
            WindowLen = i - lptr + 1

            if(minLen > WindowLen):

                minLen = WindowLen
                start_index = lptr # New starting index of window

            
    if(start_index == -1):
            return 0

    return string[start_index : start_index + minLen]

    
    # pattern_dict = dict(Counter(pattern))
    # req_len = len(pattern)

    # count = 0    

    # Window = {}

    # lptr, rptr, minLen = 0, 0, 0

    # while(rptr < len(string)):

    #     if(count == req_len):
    #         minLen = (rptr - lptr + 1)

    #         if(string[lptr] not in pattern_dict):
    #             lptr += 1
    #         elif(Window[string[lptr]] > pattern_dict[string[lptr]]):
    #             lptr += 1

    #     if(string[rptr] not in Window):
    #         Window[string[rptr]] = 1
    #     else:
    #         Window[string[rptr]] += 1

    #     if(Window[string[rptr]] in pattern_dict and Windows[string[rptr]] <= pattern_dict[string[rptr]]):
    #         count += 1
        
    #     rptr += 1

    # return minLen

        




def main():
    string = input("Enter a string: ")
    pattern  = input("Enter the pattern to search: ")

    minLen = MinWindowSub(string, pattern)

    print(f"Minimum length in string where pattern is present: {len(minLen)}")

if __name__ == "__main__":
    main()