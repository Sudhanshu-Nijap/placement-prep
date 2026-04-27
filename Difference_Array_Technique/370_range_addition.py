def range_addition( nums,updates):
    for start , end , val in updates:
        nums[start] += val
        if  end+1 < len(nums):
            nums[end+1] -= val
            
    for i in range(len(nums)-1):
        nums[i+1] = nums[i]+nums[i+ 1]
        
    return nums
    
nums = [0,0,0,0,0]
updates = [(1,3,2),(2,4,3),(0,2,-2)]

print(range_addition(nums,updates))