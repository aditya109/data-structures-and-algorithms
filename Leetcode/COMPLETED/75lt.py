from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        p0 = 0
        pl =length-1

        index = 0

        while index <= pl:
            if nums[index] == 0:
                nums[index], nums[p0] = nums[p0], nums[index]
                p0+=1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[pl] = nums[pl], nums[index]
                pl-=1
            else:
                index += 1
            
        return nums

print(Solution().sortColors([2,0,1]))
        