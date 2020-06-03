class Solution:
    def fib(self, N: int) -> int:
        start1, start2 = 0, 1

        res = 0
        if N==0:
            return 0
        while N>0:
            N = N-1
            start1 = start2
            start2 = res
            res = start1 + start2
        return res
    

print(Solution().fib(4))