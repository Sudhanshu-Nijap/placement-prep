def maxPoints(arr,k):
    i = k-1
    j = len(arr)-1
    lsum = 0
    rsum = 0

    for x in range(k):
        lsum += arr[x]

    maxsum = lsum

    while i>=0:
        lsum -= arr[i]
        rsum += arr[j]
        totalsum = lsum + rsum
        maxsum = max(maxsum, totalsum)
        i-=1
        j-=1

    return maxsum

arr = [1,2,3,4,5,6,1]
k = 3
print(maxPoints(arr,k))