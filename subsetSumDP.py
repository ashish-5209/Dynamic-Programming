def subset(lis, n, s):

    dp = [[False for i in range(s+1)]
            for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1,n+1):
        for j in range(1,s+1):

            if lis[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j-lis[i-1]] or dp[i-1][j]

    return dp[n][s]

lis = [3, 34, 4, 12, 5, 2]
s = 9
n = len(lis)

print(subset(lis, n, s))
