def countnumberrsubarray(nums, k):
    prefix_dict = {0:1}
    prefix_sum = 0
    count = 0

    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            prefix_sum += 1
        else:
            prefix_sum += 0

        if (prefix_sum - k) in prefix_dict:
            count += prefix_dict[(prefix_sum - k)]
            
        prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1
        
    return count

nums = [1,1,2,1,1]
k = 3
print(countnumberrsubarray(nums, k))