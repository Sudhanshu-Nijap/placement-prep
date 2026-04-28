def longestsubstringkchars(s,k):
    l = 0
    maxlen = -1
    char_dict = dict()
    
    for r in range(len(s)):
        char_dict[s[r]] = char_dict.get(s[r], 0) + 1
        
        while len(char_dict) > k:
            char_dict[s[l]] -= 1
            
            if char_dict[s[l]] == 0:
                del char_dict[s[l]]
                
            l+=1
            
        if len(char_dict) == k:
            maxlen = max(maxlen, r-l+1)
            
    return maxlen
    
    
    
s = "aabaaab"
k = 2
print(longestsubstringkchars(s,k))