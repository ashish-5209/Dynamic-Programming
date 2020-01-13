def optimal(arr, i, j):
    if (i+1) == j:
        return max(arr[i], arr[j])
    return max((arr[i] + min(optimal(arr, i+2, j), optimal(arr, i+1, j-1))),
                (arr[j] + min(optimal(arr, i+1, j-1), optimal(arr, i, j-2))))

def optimal1(arr, i, j, s):
    if (i+1) == j:
        return max(arr[i], arr[j])
    return max(s - optimal1(arr, i+1, j, s-arr[i]), s - optimal1(arr, i, j-1, s-arr[j]))

def optimal3(arr):
    n = len(arr)
    table = [[0 for i in range(n)]
                for i in range(n)]
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap
            x = 0
            if((i + 2) <= j):
                x = table[i + 2][j]
            y = 0
            if((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if(i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y),
                              arr[j] + min(y, z))
    return table[0][n - 1]

def optimal4(arr, i, j, dp):

    if (i+1) == j:
        return max(arr[i], arr[j])

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = max((arr[i] + min(optimal4(arr, i+2, j, dp), optimal4(arr, i+1, j-1, dp))),
                (arr[j] + min(optimal4(arr, i+1, j-1, dp), optimal4(arr, i, j-2, dp))))
    return dp[i][j]

def optimal5(arr, i, j, s, dp):
    if (i+1) == j:
        return max(arr[i], arr[j])
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = max(s-optimal5(arr, i+1, j, s-arr[i], dp),
                    s-optimal5(arr, i, j-1, s-arr[j], dp))

    return dp[i][j]

arr = [ 8, 15, 3, 7 ]
print(optimal(arr, 0, len(arr)-1))

print(optimal1(arr, 0, len(arr)-1, sum(arr)))

print(optimal3(arr))
n = len(arr)
dp = [[-1]*n for i in range(n)]
print(optimal4(arr, 0, len(arr)-1, dp))
print(dp[0][n-1])
dp = [[-1]*n for i in range(n)]
print(optimal5(arr, 0, n-1, sum(arr), dp))
