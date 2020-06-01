"""Let's define digit degree of some positive integer as the number of times we need to replace this number with the sum of its digits until we get to a one digit number.

Given an integer, find its digit degree.

Example

For n = 5, the output should be
digitDegree(n) = 0;
For n = 100, the output should be
digitDegree(n) = 1.
1 + 0 + 0 = 1.
For n = 91, the output should be
digitDegree(n) = 2.
9 + 1 = 10 -> 1 + 0 = 1."""

def digitDegree(n):
    degree = 0

    while len(str(n))!=1:
        degree+=1
        sum_number = 0
        while n!=0:
            sum_number+=n%10
            n//=10
        n = sum_number
        print(n)

    return degree

print(digitDegree(9))

