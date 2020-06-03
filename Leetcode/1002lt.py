from typing import List
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 0:
            return []
        elif len(A) == 1:
            return list(A[0])
        else:
            
            freq_map = {}
            
            for ch in A[0]:
                if ch in freq_map:
                    freq_map[ch] += 1
                else:
                    freq_map[ch] = 1
            
            for string in A[1:]:
                for k, v in freq_map.items():
                    if string.count(k) == 0:
                        freq_map.pop(k)
                    elif string.count(k) <= v:
                        freq_map[k] = string.count(k)
        return -1

if __name__ == "__main__":
    inputString = ["bella","label","roller"]
    print(Solution().commonChars(inputString))