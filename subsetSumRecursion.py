def subset(lis, n, s):

    if s == 0:
        return True
    if n == 0 and s != 0:
        return False

    if lis[n-1] > s:
        return subset(lis, n-1, s)

    return subset(lis, n-1, s-lis[n-1]) or subset(lis, n-1, s)

lis = [3, 34, 4, 12, 5, 2]
s = 9
n = len(lis)

print(subset(lis, n, s))
