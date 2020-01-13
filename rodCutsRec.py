def rods(n, a, b, c):
    if n < 0:
        return -1
    if n == 0:
        return 0

    res = max(rods(n-a, a, b, c),
                    rods(n-b, a, b, c),
                    rods(n-c, a, b, c))

    if res == -1:
        return -1
    else:
        return res+1

print(rods(5, 1, 2, 3))
