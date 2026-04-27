def quick_sort(l,r,arr):
    if l>=r:
        return arr
    
    pivot_idx = partition(l,r,arr)
    quick_sort(l,pivot_idx-1,arr)
    quick_sort(pivot_idx+1,r,arr)

def partition(l,r,arr):
    pivot = arr[l] # first ele
    i = l
    j = r

    while i<j:
        while arr[i]<=pivot and i<=r:
            i+=1

        while arr[j]>pivot and j>=l:
            j-=1

        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break

    arr[l],arr[j] = arr[j], arr[l]
    return j

arr = [5, 2, 1, 6, 4]
quick_sort(0, len(arr) - 1,arr)
print(arr)
            
                
