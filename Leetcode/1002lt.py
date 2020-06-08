from typing import List
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        freq_map = dict()

        for i in A[0]:
            if i in freq_map:
                freq_map[i]+=1
            else:
                freq_map[i]=1

        if len(A) == 1:
            return freq_map.keys()
        else:
            pass


        
        
       
A = [["bella","label","roller"], ["cool","lock","cook"]]
for i in A:
    print(Solution().commonChars(i))