import math
def sum_square_difference(n:int)-> int:
    sum_squares = ((n+1)*(2*n+1)*n)//6
    square_sums = math.pow((n*(n+1))//2, 2)
    return int(abs(square_sums-sum_squares))
print(sum_square_difference(100))