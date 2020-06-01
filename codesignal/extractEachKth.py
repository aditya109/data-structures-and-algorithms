def extractEachKth(inputArray, k):
    count = 1
    result = []
    for e in inputArray:
         if count % k != 0:
             result.append(e)
         count+=1
    return result






print(extractEachKth( [2, 4, 6, 8, 10], 1))