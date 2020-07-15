from typing import List
class Solution:
    def runningsum_of_elements(self, nums: List[int]) -> List[int]:
        sum_of_elements = 0
        for idx, i in enumerate(nums):
            sum_of_elements+=i
            nums[idx] = sum_of_elements
        return nums




print(Solution().runningsum_of_elements([1,2,3,4]))