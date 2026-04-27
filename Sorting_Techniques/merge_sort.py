def merge_sort(l,r,arr):
    if l>=r:
        return arr
        
    mid = (l+r)//2
    merge_sort(l,mid,arr)
    merge_sort(mid+1,len(arr)-1,arr)
    
    merge(l,mid,r,arr)
    
def merge(l,mid,r,arr):
    i = l
    j = mid+1
    res = []
    
    while i<=mid and j<=r:
        if arr[i] < arr[j]:
            res.append(arr[i])
            i+=1
        else:
            res.append(arr[j])     
            j+=1
            
    while i<=mid:
        res.append(arr[i])
        i+=1   
        
    while j<=r:
        res.append(arr[j])
        j+=1  
              
    x = 0
    for k in range(l,r+1):
        arr[k] = res[x]
        x+=1
        
arr = [5, 2, 1, 6, 4]
merge_sort(0, len(arr) - 1, arr)
print(arr)
    
                