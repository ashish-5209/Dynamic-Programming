def lcs(s1, s2, m, n, memo):
    if memo[m][n] != -1:
        return memo[m][n]
    if m == 0 or n == 0:
        memo[m][n] = 0
    elif s1[m-1] == s2[n-1]:
        memo[m][n] = 1 + lcs(s1, s2, m-1, n-1, memo)
    else:
        memo[m][n] = max(lcs(s1, s2, m, n-1, memo), lcs(s1, s2, m-1, n, memo))
    return memo[m][n]

X = "AGGTAB"
Y = "GXTXAYB"
memo = [[-1]*(len(Y)+1) for i in range(len(X)+1)]
print("Length of LCS is ", lcs(X , Y, len(X), len(Y), memo))
