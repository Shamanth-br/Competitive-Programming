class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = nums[::]
        nums.sort()
        l,r = 0, len(nums)-1
        while(l < r):
            if nums[l] + nums[r] == target:
                i = nums2.index(nums[l])
                nums2.pop(i)
                j = nums2.index(nums[r])
                if i <= j:
                    return [i,j+1]
                else: return[j,i] 
            elif nums[l]+nums[r] > target:
                r -= 1
            else:
                l += 1
        return