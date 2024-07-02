class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum,right_sum,curr = [],[],0
        for num in nums:
            left_sum.append(curr)
            curr += num

        for num in nums:
            curr -= num
            right_sum.append(curr)

        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        
        return -1
    
            
        