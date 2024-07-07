class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i,count,size = 0,0,len(nums)

        while(i < size-count):
            if nums[i] == 0:
                count += 1
                nums[i:] = nums[i+1:]
                nums.append(0)
            else:
                i += 1
            