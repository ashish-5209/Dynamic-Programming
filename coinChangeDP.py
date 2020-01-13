def coin(arr, n, s):
    dp = [[0]*(n+1) for i in range(s+1)]
    for i in range(n+1):
        dp[0][i] = 1
    for i in range(1, s+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1]
            if arr[j-1] <= i:
                dp[i][j] += dp[i-arr[j-1]][j]
    return dp[s][n]

arr = [2, 5, 3, 6]
s = 10
print(coin(arr, len(arr), s))
