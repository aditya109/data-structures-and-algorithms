def lcs(x, y, m, n):
    t = [[None]*(m+1)]*(n+1)
    for i in range(0, m+1):
        for j in range(0, n+1):
            if i==0 or j==0:
                t[i][j]=0
            elif x[i-1] == y[j-1]:
                t[i][j] = 1+t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    print(t)
    return t[m][n]
def buildPalindrome(st):
    return len(st)-lcs(st, st[::-1], len(st), len(st))
st = "abaa"
print(buildPalindrome(st))

