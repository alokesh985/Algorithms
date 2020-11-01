# Function will return index to remove that will make a string a palindrome

def palindromeIndex(s):
    
    if(s == s[::-1]):
        return -1
    
    i = 0
    j = len(s) - 1
    
    while(i <= j):
        
        if (i + 1 == j) or (i == j):
            return j
        
        elif(s[i] == s[j]):
            i += 1
            j -= 1
          
        elif(s[i] != s[j]):
            
            if(s[i] == s[j - 1] and s[j] == s[i + 1]):
                if(s[j - 1] != s[i + 2]):
                    return j
                
                elif(s[i + 1] != s[j - 2]):
                    return i
            
            elif(s[i] == s[j - 1]):
                return j
            
            else:
                return i
        

