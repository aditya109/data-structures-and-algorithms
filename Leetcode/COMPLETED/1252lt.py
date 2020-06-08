from typing import List


class Solution:
    def increaseRowElements(self, n: int, m: int, null_matrix: List[List[int]], row: int) -> List[List[int]]:
        for j in range(m):
            null_matrix[row][j] += 1
        return null_matrix

    def increaseColumnElements(self, n:int, m:int, null_matrix:List[List[int]], column:int) -> List[List[int]]:
        for i in range(n):
            null_matrix[i][column]+=1
        return null_matrix

    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        null_matrix = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(0)
            null_matrix.append(temp)        
        
        odd_counter = 0
        
        for index in indices:
            null_matrix = self.increaseRowElements(n, m, null_matrix, index[0])
            null_matrix = self.increaseColumnElements(n, m, null_matrix, index[1])

        for row in null_matrix:
            for element in row:
                if element % 2 != 0:
                    odd_counter+=1
        return odd_counter

print(Solution().oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))
