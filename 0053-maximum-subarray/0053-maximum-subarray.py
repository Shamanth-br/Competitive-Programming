class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = float('-inf')
        current = 0
        for num in nums:
            current += num
            largest = max(largest,current)
            if current < 0:
                current = 0
        return largest 