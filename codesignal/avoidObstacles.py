def isMultipleOf(inputArray, n):
    for i in inputArray:
        if i%n==0:
            return False
    return True

def avoidObstacles(inputArray):

    i = 2
    while not isMultipleOf(inputArray, i):
        i+=1
    return i


print(avoidObstacles([19, 32, 11, 23]))