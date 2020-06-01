def longest_common_subsequence(x, y, m, n):
    t = [[0]*(n+1)]*(m+1)

    for i in range(m+1):
        for j in range(n+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1+t[i-1][j-1]
            else: t[i][j] = max(t[i][j-1], t[i-1][j])    
            