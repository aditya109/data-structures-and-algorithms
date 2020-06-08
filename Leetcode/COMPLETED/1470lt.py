from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        temp = []

        for idx, num in enumerate(nums[:len(nums)//2]):
            temp.append(nums[idx])
            temp.append(nums[idx+n])
        return temp

print(Solution().shuffle(nums = [2,5,1,3,4,7], n = 3))