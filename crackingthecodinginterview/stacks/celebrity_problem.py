"""In a party of N people, only one person is known to everyone. Such a person may be present in the party, if yes, (s)he doesn’t know anyone in the party. We can only ask questions like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.

Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 0, 0, 0},
           {0, 0, 1, 0} }
Output:id = 2


Input:
MATRIX = { {0, 0, 1, 0},
           {0, 0, 1, 0},
           {0, 1, 0, 0},
           {0, 0, 1, 0} }
Output: No celebrity

"""


class Solution:
    def __init__(self):
        pass

    def findCelebrity(self, matrix):
        stack = [i for i in range(len(matrix))]
        while len(stack) >= 2:
            a, b = stack.pop(), stack.pop()
            a_knows_b = matrix[a][b] 
            b_knows_a = matrix[b][a]
            if a_knows_b == 0:
                stack.append(a)
            if b_knows_a == 0:
                stack.append(b)
        if MATRIX[stack[0]].count(1) > 0: 
            return "No celebrity"
        return stack[0]

MATRIX = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 1, 0, 0],
          [0, 0, 1, 0]]

print(Solution().findCelebrity(MATRIX))
