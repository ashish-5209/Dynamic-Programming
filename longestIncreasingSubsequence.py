def longest(arr, n):

    dp = [1]*n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    m = 0

    for i in dp:
        m = max(m, i)

    return m

arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print("Length of lis is", longest(arr, n))
