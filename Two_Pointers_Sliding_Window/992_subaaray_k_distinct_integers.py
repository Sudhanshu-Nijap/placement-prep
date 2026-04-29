# Brute Force using sliding window template
3

class Solution:
    def subarraysWithKDistinct(self, nums, k):
        count = 0
        for i in range(len(nums)):
            num_set = set()
            for j in range(i,len(nums)):
                num_set.add(nums[j]) 
                if len(num_set) == k:
                    count+=1
                
        return count

# Optimal using sliding window and dictionary 
# trick if it is asked for exactly k distinct elements then use this formula
# (at most k) - (at most k-1)

class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return self.subarray(nums,k) - self.subarray(nums,k-1)
        
    def subarray(self,nums,k):
        count = 0
        l = 0
        num_dict = dict()

        for r in range(len(nums)):
            num_dict[nums[r]] = num_dict.get(nums[r], 0) + 1

            while len(num_dict) > k:
                num_dict[nums[l]] -= 1

                if num_dict[nums[l]] == 0:
                    del num_dict[nums[l]]

                l+=1    

            if len(num_dict) <= k:
                count+=(r-l+1)
                    
        return count
        

nums = [1,2,1,2,3]
k = 2
print(Solution().subarraysWithKDistinct(nums,k))