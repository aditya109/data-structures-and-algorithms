def longest_substring_with_k_distinct_characters(s, k):
    n = len(s)
    output = ""
    for i in range(0,n):
        distinct_chars = 0
        count = [0]*26
        temp = ""
        for j in range(i, n):
            temp = temp + s[j]
            if count[ord(s[j])-97] == 0:
                distinct_chars +=1
            count[ord(s[j])-97] += 1
            if distinct_chars == k and len(output) < len(temp):
                output = temp
                break
    return temp

print (longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
