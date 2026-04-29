def numbersubstringcontain3chars(s):
    count = 0
    
    for i in range(len(s)):
        char_set = set()
        for j in range(i,len(s)):
            char_set.add(s[j])
            if len(char_set) == 3:
                count += (len(s)-j)
                break
      
    return count
    
def numbersubstringcontain3chars(s):
    count = 0
    last_seen = {'a':-1,'b':-1,'c':-1}
    idx = -1

    for r in range(len(s)):
        last_seen[s[r]] = r 

        if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1:
            if (last_seen['a'] < last_seen['b']) and (last_seen['a'] < last_seen['c']):
                idx = last_seen['a']
            elif (last_seen['b'] < last_seen['a']) and (last_seen['b'] < last_seen['c']):
                idx = last_seen['b']
            else:
                idx = last_seen['c']

        count += (idx + 1)
        
    return count

def numbersubstringcontain3chars(s):
    count = 0
    last_seen = {'a':-1,'b':-1,'c':-1}
    idx = -1

    for r in range(len(s)):
        last_seen[s[r]] = r 

        if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1:
            count += min(last_seen.values()) + 1
        
    return count

s = "abcabc"
print(numbersubstringcontain3chars(s))