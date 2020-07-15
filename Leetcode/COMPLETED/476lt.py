"""
Given a positive integer num, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""
class Solution:
    def findComplement(self, num: int) -> int:
    	num_str = str(bin(num))[2:]
    	res = ""
    	for i in num_str:
    		if int(i) == 0:
    			res = res + "1"
    		else:
    			res = res + "0"
    	return int(res, 2)
print(Solution().findComplement(num = 5))