class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = nums[0]
        pre,post,zero = 1,1,0
        j = len(nums) - 1
        
        if j == 0:
            return nums[j]
        for i in range(len(nums)):
            if nums[i] == 0:
                zero = 1
            pre *= nums[i] 
            post *= nums[j] 
            largest = max(pre,post,largest)
            if nums[i] == 0:
                pre = 1
            if nums[j] == 0:
                post = 1
            print('pre,post,largest = ',(pre,post,largest))
            j -= 1
        if largest < 0 and zero == 1:
            return 0
        
        return largest
                    
            
            