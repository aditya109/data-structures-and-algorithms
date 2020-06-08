class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count("1")

print(Solution().hammingWeight("00000000000000000000000000001011"))