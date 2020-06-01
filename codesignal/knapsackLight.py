def knapsackLight(value1, weight1, value2, weight2, maxW):
    objects = []
    objects.append((weight1, value1))
    objects.append((weight2, value2))

    objects = (sorted(objects, key = lambda item: item[1], reverse = True))
    profit = 0
    for index, (k, v) in enumerate(objects):
        if k <= maxW:
            profit+=v
            maxW-=k
    return profit
print(knapsackLight(value1 = 5, weight1 = 2, value2 =4 , weight2 = 2, maxW = 20))