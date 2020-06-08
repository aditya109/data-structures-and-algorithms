def longest_common_subsequence(x, y, m, n):
    t = []
    for i in range(m+1):
        temp = []
        for j in range(n+1):
            temp.append(0)
        t.append(temp)

    for i in range(m+1):
        for j in range(n+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1+t[i-1][j-1]
            else: t[i][j] = max(t[i][j-1], t[i-1][j])    
    print(t)
    return t[m][n]

def longest_common_substring(x, y, m, n):
    t = []
    for i in range(m+1):
        temp = []
        for j in range(n+1):
            temp.append(0)
        t.append(temp)
    result = 0
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0: t[i][j] = 0
            elif x[i-1] == y[j-1]:
                t[i][j] = 1+t[i-1][j-1]
                result = max(result, t[i][j])
            else: t[i][j] = 0   
    return result
s1 = "OldSite:GeeksforGeeks.org"
s2 = "NewSite:GeeksQuiz.com"
print(longest_common_substring(s1, s2, len(s1), len(s2)))