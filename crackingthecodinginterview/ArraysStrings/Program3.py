"""
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr 3ohn Smith 13
Output: "Mr%203ohn%20Smith"
"""

import os
import random
import string
import time
import traceback
from essential_generators import DocumentGenerator


class Solution:
    def __init__(self):
        self.gen = DocumentGenerator()

    def my_code(self, sentence):
        index = 0
        sentence = list(sentence)
        length = len(sentence)
        while index != length:
            if sentence[index] == " ":
                sentence[index] = "%20"
            index += 1
        res = ""
        for c in sentence:
            res = res + c
        return res

    def ideal_code(self, sentence):
        return sentence.replace(" ", "%20")

    def test_my_code(self):
        start_time = time.time()
        test_case = 15
        successful_count = 0
        failed_count = 0
        for iteration in range(1, test_case+1):
            print("_______________________________________________________________________________________________")
            try:
                test_sentence = self.gen.paragraph()
                print(f"Executing test case {iteration}: {test_sentence}")
                my_result = self.my_code(test_sentence)
                ideal_result = self.ideal_code(test_sentence)
                assert my_result == ideal_result
                successful_count += 1
                print(f"\nTest case {iteration} passed ! ✔️")
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

    input("\n\n\nPress enter to exit 🚀...")

    # clearing screen
    if os.name == "nt":
        _ = os.system('cls')
