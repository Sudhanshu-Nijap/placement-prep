def characterReplacement(s, k):
    maxlen = 0
    # char_max = 0
    for i in range(len(s)):
        char_dict = dict()
        for j in range(i, len(s)):
            char_dict[s[j]] = char_dict.get(s[j], 0) + 1
            char_max = max(char_dict.values())
            changes = (j-i+1) - char_max # (total len of a substrin) - char_max

            if changes <= k:
                maxlen = max(maxlen, j-i+1)
            else:
                break

    return maxlen

def characterReplacement(s, k):
    char_dict = dict()
    maxlen = 0
    char_max = 0
    l = 0

    for r in range(len(s)):
        char_dict[s[r]] = char_dict.get(s[r], 0) + 1

        char_max = max(char_dict[s[r]], char_max)

        # while (r-l+1) - char_max > k:
        if (r-l+1) - char_max > k: # optimized
            char_dict[s[l]] -= 1
                
            if char_dict[s[l]] == 0:
                del char_dict[s[l]]

            l+=1
        maxlen = max(maxlen, (r-l+1))
            
    return maxlen


s = "AABABBA"
k = 1
print(characterReplacement(s,k))