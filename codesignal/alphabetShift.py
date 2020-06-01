def alphabeticShift(inputString):
    
    inputString = list(inputString)
    length = len(inputString)

    for index in range(length):
        next_chr = ord(inputString[index])+1
        if next_chr == 123:
            next_chr = 97
        inputString[index] = chr(next_chr)
    return "".join(inputString)

print(alphabeticShift("crazy"))