# Intuition:

# Take one element and insert it into the correct position in the sorted part.

# Algorithm:

# Assume first element is sorted
# Pick next element
# Compare with previous elements
# Shift larger elements to the right
# Insert element in correct position
# Repeat

# Complexity:
# Time: O(n^2)
# Space: O(1)

def insertion_sort(arr):
    n = len(arr)

    for i in range(n):
        j = i
        while j>0 and arr[j-1]>arr[j]:
            temp = arr[j-1]
            arr[j-1]= arr[j]
            arr[j] = temp
            j -= 1

    return arr

arr = [5,2,1,6,4,7,0,-2]    
print(insertion_sort(arr))