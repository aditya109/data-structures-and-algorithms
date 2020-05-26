"""
Knapsack 0/1 : Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
"""

# Solution : Memoized

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

