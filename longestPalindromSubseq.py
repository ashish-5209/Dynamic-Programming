def palindrom(X, n):
    dp = [[0]*(n+1) for i in range(n+1)]
    Y = X[::-1]

    for i in range(1,n+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    #return dp[n][n]

    res = ""
    i = n
    j = n
    while i > 0 and j > 0:
        if dp[i][j] == 1 + dp[i-1][j-1]:
            res += X[i-1]
            i -= 1
            j -= 1

        elif dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            j -= 1
    return(dp[n][n], res)
seq = "GEEKSFORGEEKS"
print(palindrom(seq, len(seq)))
