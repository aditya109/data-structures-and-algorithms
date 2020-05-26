"""
Knapsack 0/1 : Solution Memoized
"""
weights = [1,3,4,5]
values = [1,4,5,7]
capacity = 7
n = len(weights)
cache_table = [[-1] * (capacity + 1)] * (n + 1)

def knapsack_M (weights, values, capacity, n):
    if n == 0 or capacity == 0: return 0
    if cache_table[n][capacity] != -1: return cache_table[n][capacity]

    if weights[n-1] <= capacity:
        cache_table[n][capacity] = max(values[n-1]+knapsack_M(weights, values, capacity-weights[n-1], n-1), knapsack_M(weights, values, capacity, n-1))
    else:
        cache_table[n][capacity] = knapsack_M(weights, values, capacity, n-1)
    return cache_table[n][capacity]
print(knapsack_M(weights, values, capacity, n))