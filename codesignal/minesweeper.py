

def minesweeper(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    result = []
    for row in range(rows):
        temp = []
        for column in range(columns):
            l = -matrix[row][column]
            for x in [-1, 0, 1]:
                for y in [-1, 0, 1]:
                    if 0<=row+x<rows and 0<=column+y<columns:
                        l+=matrix[row+x][column+y]
            temp.append(l)
        result.append(temp)
    return result



matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
print(minesweeper(matrix))