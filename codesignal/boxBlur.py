def boxBlurImpl(image, lb_row, lb_column, up_row, up_column):
    temp = 0
    for i in range(lb_row, up_row+1):
        temp += sum(image[i][lb_column:up_column+1])
    return temp // 9

def boxBlur(image):
    rows = len(image)
    columns = len(image[0])

    result_rows = rows-2
    result_columns = columns-2
    result = []
    for i in range(result_rows):
        temp = []
        for j in range(result_columns):
            lb_row, lb_column = i, j
            up_row, up_column = i+2, j+2
            temp.append(boxBlurImpl(image, lb_row, lb_column, up_row, up_column))
        result.append(temp)
    return result
image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]

print(boxBlur(image))