def fibonacci_upto(n: int) -> int:
    first = 1
    second = 2
    sum = 2
    while first+second <= n:
        third = first+second
        first = second
        second = third
        if third % 2 == 0:
            sum += third
    print(sum)

fibonacci_upto(4000000)
