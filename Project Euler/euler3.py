import math
def check_prime(n:int)-> int:
    for i in range(int(math.sqrt(n)),1, -1):
        if n%i == 0:
            return False
    return True
def largest_prime_factor(n:int):
    max = 0
    i = 2
    while i <= n :
        if n%i == 0:
            n = n//i
            if check_prime(i):
                max = i
        i+= 1
    print (max)

largest_prime_factor(600851475143 )