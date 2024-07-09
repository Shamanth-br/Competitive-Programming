class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # Determine which part is sorted
            if nums[l] <= nums[mid]:  # Left part is sorted
                if nums[l] <= target < nums[mid]:  # Target is in the left part
                    r = mid - 1
                else:  # Target is in the right part
                    l = mid + 1
            else:  # Right part is sorted
                if nums[mid] < target <= nums[r]:  # Target is in the right part
                    l = mid + 1
                else:  # Target is in the left part
                    r = mid - 1

        return -1
