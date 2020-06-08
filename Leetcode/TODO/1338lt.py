# TODO

from typing import List

class Solution:
    def sum_map(self, arr_frequency_map):
        sum_elements = 0
        for i in arr_frequency_map:
            sum_elements+=i[1]
        return sum_elements

    def minSetSize(self, arr: List[int]) -> int:
        arr_frequency_map = dict()
        for i in arr:
            if i in arr_frequency_map:
                arr_frequency_map[i]+=1
            else:
                arr_frequency_map[i] = 1
        
        arr_frequency_map = sorted(arr_frequency_map.items(), key = lambda kv: kv[1])
        count = 0

        length = len(arr)
        temp = len(arr)
        count = 0
        for i in arr_frequency_map[::-1]:
            if length <= temp//2: return count
            else:
                length -= arr_frequency_map.pop()[1]
                count+=1 
        return count

arr = [[3,3,3,3,5,5,5,2,2,7], [7,7,7,7,7,7], [1,9], [1000,1000,3,7], [1,2,3,4,5,6,7,8,9,10]]

for i in arr:
    print(Solution().minSetSize(i))