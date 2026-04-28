def numbersubstringcontain3chars(s):
    count = 0
    
    for i in range(len(s)):
        char_set = set()
        for j in range(i,len(s)):
            char_set.add(s[j])
            if len(char_set) == 3:
                count+=1
      
    return count
    
    
    
s = "abcabc"
print(numbersubstringcontain3chars(s))