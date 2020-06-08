from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diff_map = {}
        result = []

        for idx, n in enumerate(nums):
            if n in diff_map.keys():
                return [diff_map[n], idx]
            diff_map[target - n] = idx
print(Solution().twoSum(nums = [-3,4,3,90], target = 0))
