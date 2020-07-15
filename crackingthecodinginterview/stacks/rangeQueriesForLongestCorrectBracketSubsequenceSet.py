"""Given a bracket sequence or in other words a string S of length n, consisting of characters ‘(‘ and ‘)’. Find the length of the maximum correct bracket subsequence of sequence for a given query range. Note: A correct bracket sequence is the one that has matched bracket pairs or which contains another nested correct bracket sequence. For e.g (), (()), ()() are some correct bracket sequence.

Examples:

Input : S = ())(())(())(
        Start Index of Range = 0, 
        End Index of Range = 11
Output : 10
Explanation:  Longest Correct Bracket Subsequence is ()(())(())

Input : S = ())(())(())(
        Start Index of Range = 1, 
        End Index of Range = 2
Output : 0
"""

class Solution:
    def __init__(self):
        pass

    def range_Queries_For_Longest_Correct_Bracket_Subsequence_Set_using_counter(self, s):
        result = ""
        temp = ""
        idx = 0
        length = len(s)
        balance = 0
        while idx != length:
            if s[idx] == "(":
                balance+= -1
                temp = temp + "("
            elif s[idx] == ")":
                balance+= 1
                temp = temp + ")"
            if balance > 0:
                balance, temp = 0, ""
            if balance == 0:
                result = result + temp
                temp = ""
            print(f"Current Character = {s[idx]}, Balance = {balance}, Temp = {temp}, Result = {result}")
            idx += 1
        print(result)


S = "())(())(())("
print(Solution().rangeQueriesForLongestCorrectBracketSubsequenceSet(S))