class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num,0) + 1
            if num_count[num] == 2:
                return True
        return False