def summation_of_primes():
    def isPrime(x):
            result = []
            i = 1
            while i*i <= x:
                if x % i == 0:
                    result.append(i)
                    if x//i != i: 
                        result.append(x//i)
                i += 1
            return len(result) == 2
    sum_primes=0
    i = 2
    while True:
        if i >= 2_000_000:
            return sum_primes
        if isPrime(i):
            sum_primes += i
            print(i)
        i+=1    
        

print(summation_of_primes())