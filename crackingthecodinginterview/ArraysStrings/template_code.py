import os
import random
import string
import time
import traceback
from essential_generators import DocumentGenerator


class TestCaseGenerator:
    def __init__(
        self,
        sample_letters=None,
        enabled_repetition=False,
        enabled_alphanumeric=False,
        enabled_special_character=False,
    ):
        self.gen = DocumentGenerator()
        self.sample_letters = sample_letters
        self.enabled_repetition = enabled_repetition
        self.enabled_alphanumeric = enabled_alphanumeric
        self.enabled_special_character = enabled_special_character

    def parametric_test_case_init(self):
        if self.sample_letters == None:
            if self.enabled_special_character:
                self.sample_letters = (
                    string.ascii_letters + string.digits + string.punctuation
                )
            elif self.enabled_alphanumeric:
                self.sample_letters = string.ascii_letters + string.digits
            else:
                self.sample_letters = string.ascii_letters

    def generate_random_number(self, digits=None):
        range_start = 10 ** (digits - 1)
        range_end = (10 ** digits) - 1
        return random.randint(range_start, range_end)
        # print(self.test_case_gen.generate_random_number(digits=4))

    def generate_random_useful_word(self, length=None):
        return self.gen.word()
        # print(self.test_case_gen.generate_random_useful_word())

    def generate_random_useless_word(self, length=None):
        if self.enabled_repetition:
            self.parametric_test_case_init()
            sample_list = list(self.sample_letters)
            random.shuffle(sample_list)
            final_string = "".join(sample_list)
            return final_string
        else:
            return "".join(random.sample(self.sample_letters, length))
        # print(self.test_case_gen.generate_random_useless_word())

    def generate_random_sentence(self):
        return self.gen.sentence()
        # print(self.test_case_gen.generate_random_sentence())

    def generate_random_paragraph(self):
        return self.gen.paragraph()
        # print(self.test_case_gen.generate_random_paragraph())

    def generate_random_choice_from_list(self, col, choices):
        return random.sample(col, choices)


class Solution:
    def __init__(self):
        self.test_case_gen = TestCaseGenerator(
            sample_letters=None,
            enabled_repetition=False,
            enabled_alphanumeric=False,
            enabled_special_character=False,
        )

    def my_code(self, test_param):
        """Type your code here
        """
        return True

    def ideal_code(self, test_param):
        """Enter Ideal Code here
        """
        return True

    def test_my_code(self):
        """Test your code here
        """
        start_time = time.time()
        test_case = 15
        successful_count = 0
        failed_count = 0
        for iteration in range(1, test_case + 1):
            print("_" * 30)
            try:
                param = ""
                print(f"Executing test case {iteration}: {param}")
                my_result = self.my_code(param)
                ideal_result = self.ideal_code(param)
                assert my_result == ideal_result
                successful_count += 1
                print(f"\nTest case {iteration} passed ! ✔️")
            except (AssertionError, IndexError) as err:
                failed_count += 1
                print(f"Test case {iteration} failed ! ❌")
                print(traceback.print_exc())
            break   # remove this break

        print("=" * 30)
        print(f"Total Test Cases Run : {test_case}")
        print(f"Total Test Cases Successful ✔️: {successful_count}")
        print(f"Total Test Cases Failed ❌: {failed_count}")
        print(
            f"Time of Execution of {test_case} test cases : {time.time() - start_time}"
        )


if __name__ == "__main__":
    # clearing screen
    if os.name == "nt":
        _ = os.system("cls")

    Solution().test_my_code()

    input("\n\n\nPress enter to exit 🚀...")

    # clearing screen
    if os.name == "nt":
        _ = os.system("cls")
