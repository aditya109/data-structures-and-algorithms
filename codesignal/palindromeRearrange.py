def palindromeRearranging(inputString):
    countOfMiddleCharacters = 0
    for ch in inputString:
        freq = inputString.count(ch)
        if freq % 2 != 0:
            countOfMiddleCharacters += 1
        if countOfMiddleCharacters > 1: 
            return False
    return True



S = "abaaaaaaaaaaaaaaaaaaaaccbccaaaaaaaaaaaaaaaaaaaaaba"
print(palindromeRearranging(S))