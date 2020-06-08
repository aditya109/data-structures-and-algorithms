from typing import List
class Solution:

    def nearest_greatest_to_right(self, arr):
        l = len(arr)
        ngr_tuple = [] 
        # ngr_tuple contains (current_number, ngr, index of ngr)

        stack = []

        for i, v in enumerate(reversed(arr)):
            if len(stack) == 0:
                stack.append((v, l-i-1))
                ngr_tuple.insert(0, (v, -1, -1))
            else:
                ngr_tuple.insert(0, (v, stack[-1][0], stack[-1][1]))
                current_max = stack.pop()
                if v > current_max[0]:
                    stack.append((v, l-i-1))
                else: 
                    stack.append(current_max)
        return ngr_tuple
        
    def nearest_greatest_to_left(self, arr):
        l = len(arr)
        ngl_tuple = [] 
        # ngl_tuple contains (current_number, ngl, index of ngl)

        stack = []

        for i, v in enumerate(arr):
            if len(stack) == 0:
                stack.append((v, i))
                ngl_tuple.append((v, -1, -1))
            else:
                ngl_tuple.append((v, stack[-1][0], stack[-1][1]))
                current_max = stack.pop()
                if v > current_max[0]:
                    stack.append((v, i))
                else: 
                    stack.append(current_max)
        return ngl_tuple
    
    def trap(self, height: List[int]) -> int:
        
        ngl_tuple, ngr_tuple = self.nearest_greatest_to_left(height), \
                                self.nearest_greatest_to_right(height)
        total_trapped_water = 0

        for index, building in enumerate(height):
            water_above_building = 0
            # print(ngl_tuple[index][1], ngr_tuple[index][1])
            if ngl_tuple[index][1] == -1 or ngr_tuple[index][1] == -1:
                water_above_building = 0
            else:
                water_above_building = min(ngl_tuple[index][1], ngr_tuple[index][1]) - building
            if water_above_building > 0:
                total_trapped_water += water_above_building
        return total_trapped_water

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))