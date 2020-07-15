"""
Write a method to decide if two strings are anagrams or not.
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

    def my_code(self, word1, word2):
        if collections.Counter(word1) == collections.Counter(word2):
            return True
        else:
            return False

    def ideal_code(self, word1, word2):
        if sorted(word1) == sorted(word2):
            return True
        else:
            return False

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
                A1 = ''.join(random.choice(seed) for i in range(N))
                A3 = ''.join(random.choice(seed) for i in range(N))
                A2 = ''.join(sorted(A1))

                word1 = random.choice([A1, A2, A3])
                word2 = random.choice([A1, A2, A3])

                print(f"Executing test case {iteration}: {word1} {word2}")
                my_result = self.my_code(word1, word2)
                ideal_result = self.ideal_code(word1, word2)
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
        print(
            f"Time of Execution of {test_case} test cases : {time.time() - start_time}")


if __name__ == "__main__":
    # clearing screen
    if os.name == "nt":
        _ = os.system('cls')

    Solution().test_my_code()

    input("\n\n\nPress enter to exit 🚀")

    # clearing screen
    if os.name == "nt":
        _ = os.system('cls')
