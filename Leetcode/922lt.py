"""Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.
Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.
You may return any answer array that satisfies this condition.

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""
from typing import List
class Solution:
    
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        odd_idx = 1
        even_idx = 0
        
        while even_idx != len(A):
            if A[even_idx] % 2 != 0:
                if A[odd_idx] % 2 == 0:
                    A[even_idx], A[odd_idx] = A[odd_idx], A[even_idx]
                else:   odd_idx+=2
            else :  even_idx+=2

        return A

arr = [4,6,8,2,5,1,3,7]
print(Solution().sortArrayByParityII(arr))

