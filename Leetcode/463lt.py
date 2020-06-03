from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        block_perimeter = 0
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] != 0:
                    if i-1 < 0 or grid[i-1][j] == 0: block_perimeter+=1 
                    if j-1 < 0 or grid[i][j-1] == 0: block_perimeter+=1
                    if j+1 == columns or grid[i][j+1] == 0: block_perimeter+=1 
                    if i+1 == rows or grid[i+1][j] == 0: block_perimeter+=1 
        return block_perimeter

grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]
print(Solution().islandPerimeter(grid))