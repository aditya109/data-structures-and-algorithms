from typing import List
class Solution:
    def findFirstOccurrence(self, nums:List[int], target:int)->int:
        left, right = 0, len(nums)-1
        result = -1
        while left<=right:
            mid = left + (right-left)//2

            if target == nums[mid]:
                result = mid
                right = mid-1
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return result


    def findLastOccurrence(self, nums:List[int], target:int)->int:
        left, right = 0, len(nums)-1
        result = -1
        while left<=right:
            mid = left + (right-left)//2

            if target == nums[mid]:
                result = mid
                left = mid + 1
            elif target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return result
        

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findFirstOccurrence(nums, target), \
            self.findLastOccurrence(nums, target)]

print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))