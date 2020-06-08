from typing import List
from heapq import heappop, heapify, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        temp = []
        heapify(temp)
        for stone in stones:
            heappush(temp, -stone)
        
        while len(temp) > 1:
            stone1 = -heappop(temp)
            stone2 = -heappop(temp)
            if stone1 != stone2:
                heappush(temp, -abs(stone1-stone2))

        if len(temp) == 0:
            return 0
        return temp[0]
        


print(Solution().lastStoneWeight([2,2]))