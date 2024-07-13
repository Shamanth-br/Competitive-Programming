class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        size = len(nums)-1
        if len(nums) < 3:
            return []
        nums.sort()

        for i in range(0,size-1):
            l,r = i+1,size
            if i > 0 and nums[i-1] == nums[i]:
                continue
            while(l < r):
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    ans.add((nums[i],nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else: r -= 1
        return ans