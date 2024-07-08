class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashes = dict()
        hashes[nums[0]] = 0
        for i in range(1, len(nums)):
            needed = target - nums[i]
            try:
                return[hashes[needed], i]
            except:
                hashes[nums[i]] = i