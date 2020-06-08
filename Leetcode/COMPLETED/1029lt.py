from typing import List
from heapq import heapify, heappush, heappop

class Solution1:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        max_heap = []
        n = len(costs)
        heapify(max_heap)

        for cost in costs:
            heappush(max_heap, (-(cost[1]-cost[0]), cost))
        min_profit = 0
        for i in range(n//2):
            min_profit+=heappop(max_heap)[1][0]
        for i in range(n//2):
            min_profit+=heappop(max_heap)[1][1]
        return min_profit

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        n = len(costs)//2
        costs.sort(key=lambda x:x[0]-x[1])
        min_output = 0
        for i in range(n):
            min_output+=costs[i][0]+costs[i+n][1]
        return min_output

print(Solution().twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))