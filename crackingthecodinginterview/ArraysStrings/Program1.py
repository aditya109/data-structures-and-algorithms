"""

Implement an algorithm to determine if a string has all unique characters. 
What if you can not use additional data structures?

"""
import collections
import os
import string
import random
import time
import traceback


class Solution:
    def __init__(self):
        pass

    def checkIfStringHasUniqueCharacters1(self, s):
        for v in collections.Counter(s.upper()).values():
            if v > 1:
                return False
        return True

    def checkIfStringHasUniqueCharacters2(self, s):
        letter_list = [0 for i in range(26)]
        for char in s:
            if letter_list[ord(char.upper())-65] == 0:  letter_list[ord(char.upper())-65] = letter_list[ord(char.upper())-65] + 1
            else:   return False
        return True

    def test_my_code(self):
        start_time = time.time()
        test_case = 15
        successful_count = 0
        failed_count = 0
        for iteration in range(test_case):
            print("_______________________________________________________________________________________________")
            try:
                N = int(random.randint(1, 20))
                seed = string.ascii_letters
                A = ''.join(random.choice(seed) for i in range(N))
                print(f"Executing test case {iteration}: {A}")
                my_result = self.checkIfStringHasUniqueCharacters2(A)
                ideal_result = self.checkIfStringHasUniqueCharacters1(A)
                print(f"my_result = {my_result}")
                print(f"ideal_result = {ideal_result}")
                assert my_result == ideal_result
                successful_count += 1
                print(f"Test case {iteration} passed ! ✔️")
            except (AssertionError, IndexError) as err:
                failed_count += 1
                print(f"Test case {iteration} failed ! ❌")
                print(traceback.print_exc())
        print("=====================================================================================================")
        print(f"Total Test Cases Run : {test_case}")
        print(f"Total Test Cases Successful ✔️: {successful_count}")
        print(f"Total Test Cases Failed ❌: {failed_count}")
        print(f"Time of Execution of {test_case} test cases : {time.time() - start_time}")


if __name__ == "__main__":
    # clearing screen
    if os.name == "nt":
        _ = os.system('cls')

    Solution().test_my_code()

    input("\n\n\nPress enter to exit 🚀")

    # clearing screen
    if os.name == "nt":
        _ = os.system('cls')