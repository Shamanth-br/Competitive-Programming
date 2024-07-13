class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        flag,i = 0,0

        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        if len(nums) == 2:
            if nums[0]+1 == nums[1]:
                return([str(nums[0]) + '->' + str(nums[1]) ])
            else: return[str(nums[0]), str(nums[1])] 

        while(i < len(nums)-1):
            if flag == 0:
                j = i
                flag = 1
            
            if nums[i+1] == nums[i]+1:
                i += 1
                continue
            elif i != j:
                ans.append(str(nums[j])+'->'+str(nums[i]))
                flag = 0
            else:
                ans.append(str(nums[i]))
                flag = 0
            i += 1
    
        if not ans and flag == 1 or flag == 1 and str(nums[j]) not in ans[-1]:
            ans.append(str(nums[j])+'->'+str(nums[i]))
            return ans
        else:
            ans.append(str(nums[-1]))
            return ans