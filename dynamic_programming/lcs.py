def longest_common_subsequence(x, y, m, n):
    t = [[None]*(n+1) for i in range(m+1)] 

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif x[i-1] == y[j-1]:
                t[i][j] = 1+t[i-1][j-1]
            else: t[i][j] = max(t[i][j-1], t[i-1][j])  
    return t[m][n]

def longest_common_substring(x, y, m, n):
    t = [[None]*(n+1) for i in range(m+1)] 
    result = 0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0: t[i][j] = 0
            elif x[i-1] == y[j-1]:
                t[i][j] = 1+t[i-1][j-1]
                result = max(result, t[i][j])
            else: t[i][j] = 0   
    return result
s1 = "abc"
s2 = "ahbgdc"
print(longest_common_subsequence(s1, s2, len(s1), len(s2)))