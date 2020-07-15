"""Simplify a given algebraic string of characters, ‘+’, ‘-‘ operators and parentheses. Output the simplified string without parentheses.

Examples:

Input : "a-(b+c)"
Output : "a-b-c"

Input : "a-(b-c-(d+e))-f"
Output : "a-b+c+d+e-f" 
"""

class Solution:
    def __init__(self):
        pass

    def expression_simplification(self, s):
        variable = []
        symbols = []
        idx = 0
        s = "(" + s + ")"
        length = len(s)
        while idx != length:
            ch = s[idx]
            
            if ch == "+" or ch == "-":
                symbols.append(ch)
            

            idx += 1