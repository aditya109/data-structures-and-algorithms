import random 
def arrayChange(inputArray):
    counter = 0
    for i in range(1, len(inputArray)):
        if inputArray[i-1] >= inputArray[i]:
            diff = inputArray[i-1]-inputArray[i] + 1
            inputArray[i] += diff
            counter += diff
    return counter

arr = [6, 9, 11, 10, 4, 8, 9, 6, 11, 8]
print(arr)
print(arrayChange(arr))

