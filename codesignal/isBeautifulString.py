"""A string is said to be beautiful if each letter in the string appears at most as many times as the previous letter in the alphabet within the string; ie: b occurs no more times than a; c occurs no more times than b; etc.

Given a string, check whether it is beautiful.

Example

For inputString = "bbbaacdafe", the output should be isBeautifulString(inputString) = true.

This string contains 3 as, 3 bs, 1 c, 1 d, 1 e, and 1 f (and 0 of every other letter), so since there aren't any letters that appear more frequently than the previous letter, this string qualifies as beautiful.

For inputString = "aabbb", the output should be isBeautifulString(inputString) = false.

Since there are more bs than as, this string is not beautiful.

For inputString = "bbc", the output should be isBeautifulString(inputString) = false.

Although there are more bs than cs, this string is not beautiful because there are no as, so therefore there are more bs than as."""

def isBeautifulString(inputString):

    string_frequency_map = {}
    for i in inputString:
        if i in string_frequency_map:
            string_frequency_map[i] += 1
        else:
            string_frequency_map[i] = 1
    print(string_frequency_map)
    if len(string_frequency_map.keys()) == 1:
        if list(string_frequency_map.keys())[0] != "a":
            return False
        return True
    for k, v in string_frequency_map.items():
        if chr(ord(k)-1) in string_frequency_map.keys():
            prev = string_frequency_map[chr(ord(k)-1)]    
        else:
            prev = 0       
        print(chr(ord(k)-1), prev)        
        if k == 'a' or v <= prev:
            pass
        else: return False

    return True

print(isBeautifulString("aaa"))