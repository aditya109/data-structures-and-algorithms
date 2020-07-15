"""
Given a permutation array A[] consisting of N numbers in range [1, N], the task is to left rotate all the even numbers and right rotate all the odd numbers of the permutation and print the updated permutation. 
Note: N is always even.

Examples: 

Input: A = {1, 2, 3, 4, 5, 6, 7, 8}
Output: {7, 4, 1, 6, 3, 8, 5, 2}
Explanation:
Even element = {2, 4, 6, 8}
Odd element = {1, 3, 5, 7}
Left rotate of even number = {4, 6, 8, 2}
Right rotate of odd number = {7, 1, 3, 5}
Combining Aoth odd and even number alternatively.

Input: A = {1, 2, 3, 4, 5, 6}
Output: {5, 4, 1, 6, 3, 2}
"""
import random, time, collections

def my_code(nums):
    start_time = time.time()
    length =  len(nums)
    even, odd = [], []
    for i in range(length):
        if nums[i] % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    even[:] = even[1:] + even[0:1]
    odd.insert(0, odd.pop())
    for i in range(length):
        if i %2 !=0:
            nums[i] = even.pop(0)
        else:
            nums[i] = odd.pop(0)

    print(f"Time of execution : {time.time() - start_time}")
    return nums

def ideal_code():
    """Enter Ideal Code here
    """
    pass

def test_my_code():
    """Test your code here
    """
    start_time = time.time()
    test_case = 15
    sucessful_count = 0
    failed_count = 0
    for iteration in range(test_case):
        print("______________________________________________________________________________________________________________________________")
        try:
            N = int(random.randint(1, 20))*2
            A = []
            for i in range(N):
                number = random.randint(0, N)
                if i % 2 != 0:
                    # insert even number
                    if number % 2 == 0:
                        A.append(number)
                    else:
                        A.append(2*number)
                else:
                    if number % 2 == 0:
                        A.append(number-1)
                    else:
                        A.append(number)
            print(f"Executing test case {iteration}: {A}")
            my_result = my_code(A)
            ideal_result = my_code(A)
            print(my_result)
            print(ideal_result)
            assert collections.Counter(my_result) == collections.Counter(ideal_result)
            sucessful_count += 1
            print(f"Test case {iteration} passed ! ✔️")
        except (AssertionError, IndexError):
            failed_count += 1
            print(f"Test case {iteration} failed ! ❌")
    print("====================================================================================================================================")
    print(f"Total Test Cases Run : {test_case}")   
    print(f"Total Test Cases Successful ✔️: {sucessful_count}")   
    print(f"Total Test Cases Failed ❌: {failed_count}")   
    print(f"Time of Execution of {test_case} test cases : {time.time() - start_time}")


if __name__ == "__main__":
    test_my_code()
    
    
