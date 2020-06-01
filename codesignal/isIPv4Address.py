def checkIfNumber(n):
    print(f"checking {n}")
    flag = False
    for ch in n:
        if ch.isdigit():
            flag = True
        else:
            return False
    return flag


def isIPv4Address(inputString):
    inputString = inputString.split(".")

    if len(inputString) != 4:   return False
    else:
        for i in inputString:
            if not checkIfNumber(i):
                return False
            else:
                
                if int(i) < 0 or int(i) > 255 or i != str(int(i)):
                    return False    
        return True





ip =  "1.1.1.1.1"
print(isIPv4Address(ip))

