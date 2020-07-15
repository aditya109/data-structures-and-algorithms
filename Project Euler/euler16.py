import math
def power_digit_sum():
    res = 1
    count = 0
    while count < 1000:
        res = res *2
        count += 1
    sum_digits = 0
    res = list(str(res))

    for i in res:
        sum_digits+=int(i)


    return sum_digits
print(power_digit_sum())