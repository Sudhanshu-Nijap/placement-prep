# Brute Force: using subarray template

def subarray(nums,k):
    count = 0
    for i in range(len(nums)):
        sum_ = 0
        for j in range(i,len(nums)):
            sum_+=nums[j]
            if sum_ == k:
                count += 1
            
        
    return count
    
# Optimal: using prefix sum

def subarray(nums,k):
    prefix_dict = {0:1}
    prefix_sum = 0
    count = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if (prefix_sum - k) in prefix_dict:
            count += prefix_dict[(prefix_sum - k)]

        prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1

    return count
    

nums = [1,2,3,4,5]
print(subarray(nums,5))
            