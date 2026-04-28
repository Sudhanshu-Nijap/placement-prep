# 2-pointers using set

def lengthOfLongestSubstring(self, s: str) -> int:
    l = 0
    r = 0
    maxlen = 0
    char_set = set()

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l+=1

        char_set.add(s[r])
        maxlen = max(maxlen,r-l+1)
            
    return maxlen
        

# 2-pointers using dictionary 

def lengthOfLongestSubstring(s):
    char_dict = dict()
    maxlen = 0
    l=0

    for r in range(len(s)):
        if s[r] in char_dict and char_dict[s[r]] >= l:
            l = char_dict[s[r]] + 1

        char_dict[s[r]] = r
        maxlen = max(maxlen,r-l+1)
        
    return maxlen

s = "abcabcbb"
print(lengthOfLongestSubstring(s))