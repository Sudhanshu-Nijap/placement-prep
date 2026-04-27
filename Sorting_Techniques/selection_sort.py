# Intuition

# Find the smallest element from unsorted part and put it in correct position.

# Algorithm:

# Start from index i
# Assume current index is minimum
# Check all elements after it
# Find actual minimum
# Swap with position i
# Repeat

# Complexity:
# Time: O(n^2)
# Space: O(1)

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j]<arr[min_idx]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i]

    return arr

arr = [5,2,1,6,4]
print(selection_sort(arr))