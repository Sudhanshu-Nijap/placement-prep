# Brute Force: using subarray template

def fruitintobasket(nums):
    maxlen = 0

    for i in range(len(nums)):
        fruit_set = set()
        for j in range(i,len(nums)):
            fruit_set.add(nums[j])
            if len(fruit_set) <= 2:
                maxlen = max(maxlen, j-i+1)
            else:
                break
        
    return maxlen

Optimal: using dictionary

def fruitintobasket(nums):
    fruit_dict = dict()
    maxlen = 0
    l = 0

    for r in range(len(nums)):
        fruit_dict[nums[r]] = fruit_dict.get(nums[r], 0 ) + 1

        while len(fruit_dict) > 2:
            fruit_dict[nums[l]] -= 1

            if fruit_dict[nums[l]] == 0:
                del fruit_dict[nums[l]]

            l+=1

        maxlen = max(maxlen, r-l+1)

    return maxlen

nums = [0,1,2,2]
print(fruitintobasket(nums))