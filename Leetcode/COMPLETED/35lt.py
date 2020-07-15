from typing import List
# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums)-1
#         index = -1

#         if target > nums[right]: return right+1
#         elif target < nums[0]: return left
#         else:
#             while left <= right:
#                 mid = left + (right-left)//2
#                 if nums[mid] >= target:
#                     index = mid
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#         return index

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target: return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1                                       

        return left
print(Solution().searchInsert([1,3,5,6],5))
