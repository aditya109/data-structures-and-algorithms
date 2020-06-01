def longestDigitsPrefix(inputString):
    prefix = ""
    for i in inputString:
        if i.isdigit():
            prefix = prefix + i
        else:
            return prefix
    return prefix
print(longestDigitsPrefix("0123456789"))