from typing import List
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        
        length = len(S)
        begin, end = 0, length

        result = []
        up = None
        if S[0] == "I":
            result.append(begin)
            begin+=1
            up = True
        else: 
            result.append(end)
            end-=1
            up = False

        temp = []
        for change in S:
            if change == "I" and up:
                    up = True
                    temp.insert(0, end)
                    end -= 1
            if change == "D":
                if up == False:
                    temp.insert(0, end)
                    end -= 1
                    











print(Solution().diStringMatch("DDDIDDIIDI"))