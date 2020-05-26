def multiple_sum_under_1000():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    print(sum)

multiple_sum_under_1000()