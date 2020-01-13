def coin(arr, n, s):
    dp = [0]*(s+1)
    dp[0] = 1

    for i in range(n):
        for j in range(arr[i], s+1):
            dp[j] += dp[j-arr[i]]

    return dp[s]

arr = [2, 5, 3, 6]
s = 10
print(coin(arr, len(arr), s))
