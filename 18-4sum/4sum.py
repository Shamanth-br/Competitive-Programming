class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        size = len(nums)
        i, j, l, r = 0, 1, 2, size-1
        nums.sort()
        if size < 4:
            return []
        # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]] ;[[-2,-1,1,2],[-1,0,0,1]]
        for i in range(size-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, size-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = size - 1
                while(l < r):
                    if (l > j+1 and nums[l] == nums[l-1]):
                        l += 1
                        continue
                    if (r < size-1 and nums[r] == nums[r+1]):
                        r -= 1
                        continue
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        ans.append([nums[i],nums[j],nums[l],nums[r]] )
                        l += 1
                        r -= 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1
        return ans 