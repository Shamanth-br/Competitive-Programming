class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        size,count = len(grid[0]),0
        row = {}
        for r in grid:
            row[str(r)] = row.get(str(r),0) + 1 
     
        for i in range(size):
            col = []
            for j in range(size):
                col.append(grid[j][i])
                count += row.get(str(col),0)
              
        return count
        