"""
Knapsack 0/1 : Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
"""

# Solution : Tabulation

weights = [1,3,4,5]
values = [1,4,5,7]
capacity = 7
n = len(weights)

def knapsack01_T(weights, values, capacity, n):
    cache_table = [[0] * (capacity + 1)] * (n + 1)
    for i in range(1, n+1):
        for j in range(1, capacity+1):
            if weights[i-1] <= j:
                cache_table[i][j] = max(values[i-1]+cache_table[i-1][j-weights[i-1]], cache_table[i-1][j])
            else:
                cache_table[i][j] = cache_table[i-1][j]
    return cache_table[n][capacity]

print(knapsack01_T(weights, values, capacity, n))