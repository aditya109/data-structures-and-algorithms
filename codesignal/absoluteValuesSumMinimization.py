def absoluteValuesSumMinimization(a):

    minDiff = None
    minElement = None
    for element in a:
        temp = 0
        for e in a:
            temp += abs(element-e)
        if minDiff == None or minDiff > temp:
            minDiff = temp
            minElement = element
    return minElement