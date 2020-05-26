"""Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.


Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

"""
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        def longest_common_subsequence(x, y, m, n):
            if m == 0 or n == 0: 
                return 0; 
            elif x[m-1] == y[n-1]: 
                return 1 + longest_common_subsequence(x, y, m-1, n-1); 
            else: 
                return max(longest_common_subsequence(x, y, m, n-1), longest_common_subsequence(x, y, m-1, n)); 

        lcs_length = longest_common_subsequence(s, t, len(s), len(t))

        return max(len(s)-lcs_length, len(t)-lcs_length)

print(Solution().minSteps(s = "leetcode", t = "practice"))
