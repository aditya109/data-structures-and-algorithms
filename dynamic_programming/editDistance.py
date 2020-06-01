def editDistance(s1, s2, m, n):
    dp = [[-1]*(n+1)]*(m+1)

    for i in range(0, m+1):
        for j in range(0, n+1):
            if i == 0:
                dp[i][j] = j
            elif j == 0: dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
    for i in dp:
        print(i)


if __name__ == "__main__":
    s1 = "abc"
    s2 = "bcd"
    print(editDistance(s1, s2, len(s1), len(s2)))