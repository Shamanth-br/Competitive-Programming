class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        index,flip,max_window,l = 0,0,0,0
        
        for r in range(len(nums)):
            if nums[r] == 0 and flip == 0:
                index = r
                flip = 1
            elif nums[r] == 0 and flip == 1:
                l = index + 1
                index = r
            max_window = max(r-l,max_window)
            #print('l = ',l,'r = ',r,'max window = ',max_window)
        return max_window #[0,1,1,1,0,1,1,0,1]