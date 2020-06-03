from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_water_held = 0
        while left != right:
            water_held = (right-left) * min(height[right], height[left])
            max_water_held = max(water_held, max_water_held)
            if height[left] < height[right]:
                left += 1
            else: right -=1
        return max_water_held

print(Solution().maxArea([2,3,4,5,18,17,6]))