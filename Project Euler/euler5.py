import math
def smallest_possible_evenly_divisible_number(upper:int, lower:int):
    ans = 1
    for i in range(lower, upper+1):
        ans = int((ans*i)/math.gcd(ans, i))
    return ans

print(smallest_possible_evenly_divisible_number(20, 1))