"""
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
"""
from heapq import heappop, heapify, heappush
from typing import List
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        count = 0

        vertical_slices = []
        for i in range(w):
            if i in verticalCuts :
                vertical_slices.append(count)
                count = 1
            else:
                count += 1
            
        vertical_slices.append(count)

        maxAreaSlice = []
        heapify(maxAreaSlice)
        temp = [0]*len(vertical_slices)

        print(f"Initially temp = {temp} vertical slices = {vertical_slices}")
        for i in range(h):
            if i in horizontalCuts:
                heappush(maxAreaSlice,-max(temp))
                for j, v in enumerate(vertical_slices):
                    temp[j] = v
            else:
                for j, v in enumerate(vertical_slices):
                    temp[j] += v
        heappush(maxAreaSlice,-max(temp))
        return -heappop(maxAreaSlice)


# Solution().maxArea(h = 5, w = 2, horizontalCuts = [3,1,2], verticalCuts = [1])
print(Solution().maxArea(h = 5, w = 2, horizontalCuts = [3,1,2], verticalCuts = [1]))

"""
 # print(vertical_slices)
        for i in range(h):
            if i in horizontalCuts:
                # heappush(maxAreaSlice, -max(temp))
                # temp = [0]*len(vertical_slices)
                # for i in range(len(vertical_slices)):
                #     temp [i] += vertical_slices[i]
                pass
            else:
                pass
                # for i in range(len(vertical_slices)):
                #     temp [i] += vertical_slices[i]
            # print(i, temp, maxAreaSlice)
            print(i, end = " ")
"""
