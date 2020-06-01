import itertools

def isDifferByOneChar(a, b):
    count = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1

    return count == 1

def stringsRearrangement(inputArray):
    possible = itertools.permutations(inputArray)
    for p in possible:
        allMatch = True
        for i in range(len(p)):
            if not isDifferByOneChar(p[i], p[i+1]):
                allMatch = False
                break
        if allMatch:
            return True
    return False

print(stringsRearrangement(["aba", "bbb", "bab"]))