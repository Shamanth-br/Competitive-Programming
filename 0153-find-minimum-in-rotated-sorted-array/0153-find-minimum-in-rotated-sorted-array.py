class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        smallest = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                return min(smallest,nums[l])
            mid = (l + r) // 2
            
            # Determine which part is sorted
            if nums[l] <= nums[mid]:  # Left part is sorted
                l = mid+1
            else:  # Right part is sorted
                r = mid-1
            smallest = min(smallest,nums[mid])
        return smallest
