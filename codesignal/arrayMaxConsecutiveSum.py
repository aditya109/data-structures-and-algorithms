def arrayMaxConsecutiveSum(inputArray, k):
    sum_k = sum(inputArray[0:k])
    max_sum = sum_k

    l = len(inputArray)
    for i in range(k, l):
        max_sum = max(max_sum, sum_k)
        sum_k = sum_k - inputArray[i-k] + inputArray[i]
    max_sum = max(max_sum, sum_k)
    return max_sum



print(arrayMaxConsecutiveSum(inputArray= [963, 741, 22, 851, 399, 382, 190, 247, 494, 452, 891, 532, 795, 920, 465, 831, 344, 391, 582, 897, 763, 951, 735, 806, 320, 702, 200, 59, 870, 345, 695, 321, 817, 83, 416, 36, 914, 335, 117, 985, 690, 303, 875, 556, 292, 309, 496, 791, 509, 360, 235, 784, 607, 341], k= 23))