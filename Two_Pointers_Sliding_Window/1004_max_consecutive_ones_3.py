# Brute Force: using subarray template

def max_consective_ones(nums,k):
    maxlen = 0
    
    for i in range(len(nums)):
        zeros = 0
        for j in range(i,len(nums)):
            if nums[j] == 0:
                zeros+=1
            
            if zeros <= k:
                length = j-i+1
                maxlen = max(maxlen, length)
            else:
                break

    return maxlen

# Better: using 2-pointer

def max_consective_ones(nums,k):
    l = 0
    zeros = 0
    maxlen = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            zeros+=1
        
        while zeros>k:
            if nums[l] == 0:
                zeros-=1
            l+=1
        
        if zeros<=k:
            maxlen = max(maxlen, r-l+1)

    return maxlen

# Optimal: replaced while with if

ef max_consective_ones(nums,k):
    l = 0
    zeros = 0
    maxlen = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            zeros+=1
        
        if zeros>k:
            if nums[l] == 0:
                zeros-=1
            l+=1
        
        if zeros<=k:
            maxlen = max(maxlen, r-l+1)

    return maxlen

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(max_consective_ones(nums,k))

