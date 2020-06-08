"""Given an array of n numbers. The problem is to move all the 0’s to the end of the array while maintaining the order of the other elements. Only single traversal of the array is required.

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6}
Output : 1 2 3 6 0 0 0

Input: arr[] = {0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9}
Output: 1 9 8 4 2 7 6 9 0 0 0 0 0

"""

import random
import time
import collections
import traceback
import os
from subprocess import call

def my_code(nums):
    start_time = time.time()
    length = len(nums)
    i = 0
    while(i != length-1):
        print(nums)
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            i-=1
        i += 1

    print(f"Time of execution : {time.time() - start_time}")
    return nums


def ideal_code(arr):
    """Enter Ideal Code here
    """
    start_time = time.time()
    count = 0
    n = len(arr)

    # Traverse the array. If arr[i] is non-zero, then
    # swap the element at index 'count' with the
    # element at index 'i'
    for i in range(0, n):
        if (arr[i] != 0):
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    print(f"Time of execution : {time.time() - start_time}")

    return arr


def test_my_code():
    """Test your code here
    """
    start_time = time.time()

    test_case = 5
    sucessful_count = 0
    failed_count = 0
    for iteration in range(test_case):
        print("_______________________________________________________________________________________________")
        try:
            N = int(random.randint(1, 20))
            A = []
            for i in range(N):
                number = random.randint(0, N)
                if i % 2 != 0:
                    A.append(0)
                else:
                    A.append(number)
            print(f"Executing test case {iteration}: {A}")
            my_result = my_code(A)
            ideal_result = ideal_code(A)
            print(my_result)
            print(ideal_result)
            assert collections.Counter(
                my_result) == collections.Counter(ideal_result)
            sucessful_count += 1
            print(f"Test case {iteration} passed ! ✔️")
        except (AssertionError, IndexError) as err:
            failed_count += 1
            print(f"Test case {iteration} failed ! ❌")
            print(traceback.print_exc())
    print("====================================================================================================================================")
    print(f"Total Test Cases Run : {test_case}")
    print(f"Total Test Cases Successful ✔️: {sucessful_count}")
    print(f"Total Test Cases Failed ❌: {failed_count}")
    print(
        f"Time of Execution of {test_case} test cases : {time.time() - start_time}")

if __name__ == "__main__":
    # clearing screen
    if os.name == "nt":
        _ = os.system('cls')

    # test_my_code()
    print(my_code([0, 0, 1, 0, 6, 0]))

    input("\n\n\nPress enter to exit 🚀")

    # clearing screen
    if os.name == "nt":
        _ = os.system('cls')

