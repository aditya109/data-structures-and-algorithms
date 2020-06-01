"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
Example:

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""
arr = [3, 4, 5, 2]
sum = 9

def check_subset_sum_T(arr, sum , n):
    cache_table = [[False] * (sum+1)]*(n+1)

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if j == 0:
                cache_table[i][j] = True
            if i == 0:
                cache_table[i][j] = False
    cache_table[0][0] = True

    for i in range(1, n+1):
        for j in range(1, sum+1):
            if arr[i-1]<=j:
                cache_table[i][j] = cache_table[i-1][j-arr[i-1]] or cache_table[i-1][j]
            else:
                cache_table[i][j] = cache_table[i-1][j]
    return cache_table[n][sum]

print(check_subset_sum_T(arr, sum, len(arr)))