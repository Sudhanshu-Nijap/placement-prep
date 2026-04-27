# Intuition:

# Compare adjacent elements and keep pushing the largest element to the end in every round.

# Algorithm:

# Start from beginning of array
# Compare arr[j] and arr[j+1]
# If left > right → swap
# Continue till end
# After 1st round → largest is at last
# Repeat for remaining array (ignore last sorted part)

# Complexity:
# Time: O(n^2)
# Space: O(1)

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

arr = [5,2,1,6,4,7,0,-2]   
print(bubble_sort(arr))