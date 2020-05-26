def check_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def largest_palindrome_product():
    upper_limit = 1000
    lower_limit = 100
    maxM = -1
    for i in range(lower_limit, upper_limit):
        for j in range(lower_limit, upper_limit):
            if check_palindrome(i*j):
                maxM = max(i*j, maxM)
    return maxM


print(largest_palindrome_product())
