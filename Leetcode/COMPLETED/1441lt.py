from typing import List
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        target_length = len(target)
        integer = 1
        index = 0
        while index < target_length:
            result.append("Push")
            if integer != target[index]:
                result.append("Pop")
            else:
                index +=1
            integer += 1
        return result
print(Solution().buildArray(target = [1,3], n = 3))