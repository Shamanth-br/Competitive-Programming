class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        size,k,count = len(grid[0]),0,0
        row = []
        while(k < size):
            for i in range(size):
                count += 1
                for j in range(size):
                    if grid[j][i] != grid[k][j]:
                        count -= 1
                        break
            k += 1
            
        return count
        