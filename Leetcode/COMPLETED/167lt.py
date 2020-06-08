from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        sum_map = {}
        for index, n in enumerate(numbers):
            if n in sum_map:
                return [sum_map[n]+1, index+1]
            else:
                sum_map[target-n] = index



print(Solution().twoSum(numbers=[2,7,11,15], target=9))