class Solution:
    def sortColors(self, nums):

        length = len(nums)
        index = 0
        count_2_shifted = 0
        count = 0

        while index <= length-count_2_shifted-1:
            print(index, count_2_shifted, nums)
            if nums[index] == 0 and index != 0:
                nums.pop(index)
                nums.insert(0, 0)
                index-=1
            elif nums[index] == 2 and index != length-1:
                nums.pop(index)
                nums.append(2)
                index-=1
                count_2_shifted+=1
            index+=1
            count+=1
        return nums

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
print()
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print()
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]
