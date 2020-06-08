from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))

print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
