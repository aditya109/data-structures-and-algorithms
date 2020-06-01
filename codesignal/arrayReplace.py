def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for index in range(len(inputArray)):
        if inputArray[index] == elemToReplace:
            inputArray[index] = substitutionElem

    return inputArray

print(arrayReplace(inputArray = [1, 2, 1], elemToReplace = 1, substitutionElem = 3))
    
