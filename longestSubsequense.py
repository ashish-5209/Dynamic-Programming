def lcs(x, y):

    m = len(x)
    n = len(y)

    l = [[0]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                l[i][j] = 0
            elif x[i-1] == y[j-1]:
                l[i][j] += l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])

    return l[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y))
