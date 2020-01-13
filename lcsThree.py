def lcs(X, Y, Z, m, n, o):
    dp = [[[0]*(o+1)for i in range(n+1)]for j in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            for k in range(1, o+1):
                if (X[i-1] == Y[j-1]) and (Y[j-1] == Z[k-1]):
                    dp[i][j][k] = 1 + dp[i-1][j-1][k-1]
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    return dp[m][n][o]


X = 'AGGT12'
Y = '12TXAYB'
Z = '12XBA'

m = len(X)
n = len(Y)
o = len(Z)

print(lcs(X, Y, Z, m, n, o))
