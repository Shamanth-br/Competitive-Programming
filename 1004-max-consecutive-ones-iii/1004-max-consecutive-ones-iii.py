class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count,window_size,max_window_size,l = 0,0,0,0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
            while(zero_count > k):
                if nums[l] == 0:
                    zero_count -= 1
                l += 1
            window_size = r - l + 1
            max_window_size = max(max_window_size,window_size)
        return max_window_size