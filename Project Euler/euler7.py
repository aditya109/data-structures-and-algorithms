def primeN(n:int)->int:
    counter=1
    i = 2
    file = open("notes.txt", "w")
    while True:
        def factors(x):
            result = []
            i = 1
            while i*i <= x:
                if x % i == 0:
                    result.append(i)
                    if x//i != i: 
                        result.append(x//i)
                i += 1
            return len(result) == 2

        if factors(i):
            # print(f"")
            file.write(f"{i} {counter}\n")

            counter+=1
        if counter == 10002:
            break
        i+=1
    file.close()
    return i
print(primeN(10001))