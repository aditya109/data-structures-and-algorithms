"""
You are given a rectangular board of M × N squares. Also you are given an unlimited number of standard domino pieces of 2 × 1 squares. You are allowed to rotate the pieces. You are asked to place as many dominoes as possible on the board so as to meet the following conditions:

1. Each domino completely covers two squares.

2. No two dominoes overlap.

3. Each domino lies entirely inside the board. It is allowed to touch the edges of the board.

Find the maximum number of dominoes, which can be placed under these restrictions.

Input
In a single line you are given two integers M and N — board sizes in squares (1 ≤ M ≤ N ≤ 16).

Output
Output one number — the maximal number of dominoes, which can be placed.
"""
import pprint

pp = pprint.PrettyPrinter(indent=4)


def main():
    m, n = input().strip().split(" ")
    m, n = int(m), int(n)

    count = 0
    board = list()
    temp = list()
    for i in range(n):
        temp.append(-1)
    for i in range(m):
        board.append(temp)

    for row in range(m):

        for col in range(n):
            print(f"{board}, i = {row}, j = {col}, count = {count}")
            if board[row][col] == -1:
                # current tile is empty
                if row + 1 == m or col + 1 == n:
                    # next tile is not available
                    pass
                else:
                    if board[row][col+1] == -1:
                        # domino can be placed here horizontally
                        board[row][col] = 0
                        board[row][col+1] = 0
                        count +=1
                    elif board[row+1][col] == -1:
                        # domino can be placed here vertically
                        board[row][col] = 0
                        board[row+1][col] = 0
                        count+=1
            # print(f"{board}, i = {row}, j = {col}, count = {count}")
                
                
                


if __name__ == "__main__":
    main()