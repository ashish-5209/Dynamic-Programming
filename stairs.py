def steps(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    ans = steps(n-1) + steps(n-2) + steps(n-3)
    return ans

print(steps(4))
