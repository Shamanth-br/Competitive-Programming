class Solution:
    def maxArea(self, height: List[int]) -> int:
        width = len(height)-1
        water = min(height[0],height[-1])* width
        i,j = 0,width
        while(i < j):
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            width -= 1
            curr = min(height[i],height[j]) * width
            water = max(water,curr)
        return water
