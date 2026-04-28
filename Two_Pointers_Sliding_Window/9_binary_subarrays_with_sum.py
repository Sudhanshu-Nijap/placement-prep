def binarysubarraysum(nums, goal):
    prefix_dict = {0:1}
    prefix_sum = 0
    count = 0

    for i in range(len(nums)):
        prefix_sum += 1
        

        if (prefix_sum - goal) in prefix_dict:
            count += prefix_dict[(prefix_sum - goal)]
            
        prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1
    
    return count
        


nums = [1,0,1,0,1]
goal = 2
print(binarysubarraysum(nums, goal))