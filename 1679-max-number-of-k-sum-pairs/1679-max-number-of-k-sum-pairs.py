class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_count = {}
        count = 0
        for num in nums:
            nums_count[num] = nums_count.get(num,0) + 1
            if(k-num != num and nums_count.get(k-num,0) > 0):
                count += 1
                nums_count[num] -= 1
                nums_count[k-num] -= 1
            elif(k-num == num and nums_count.get(k-num,0) > 1):
                count += 1
                nums_count[num] -= 2
        return count