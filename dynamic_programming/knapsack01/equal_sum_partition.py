"""
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.
Examples:

arr[] = {1, 5, 11, 5}
Output: true
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false
The array cannot be partitioned into equal sum sets.
"""

arr = [1, 5, 11, 5]

def check_equal_sum_partition(arr, n):

    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    





check_equal_sum_partition(arr, len(arr))
