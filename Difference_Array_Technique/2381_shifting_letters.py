def shiftingLetters(s, shifts):
    n = len(s)
    arr = [0]*n
    for st,e,v in shifts:
        if v == 0:
            arr[st] -= 1
            if e+1 < n:
                arr[e+1] += 1
        else:
            arr[st] += 1
            if e+1 < n:
                arr[e+1] -= 1

    for i in range(n-1):
        arr[i+1] = arr[i+1] + arr[i]

    ans = ""
    for c in range(n):
        ans += chr( ((ord(s[c]) - ord('a')) + arr[c]) % 26 + ord('a') ) 
        # ord('a') => Gives the number (ASCII value) of 'a'
        # ord(s[c]) - ord('a') => Converts the character into a position (0–25)
        # 'a' → 0
        # 'b' → 1
        # 'z' → 25
        # + arr[c] => Adds how much you want to shift
        # % 26 => Keeps the value within 0–25
        # If it goes beyond 'z', it wraps back to 'a'
        # + ord('a') => Converts the number back to ASCII range
        # chr() => Converts the number back to a character

    return ans

s = "abc"
shifts = [[0,1,1],[1,2,1],[0,2,1]]

print(shiftingLetters(s,shifts))

