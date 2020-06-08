import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        res = 0
        while res <= n:
            res = int(math.pow(2, i))
            if res == n:
                return True
            i += 1
        return False

print(Solution().isPowerOfTwo(0))