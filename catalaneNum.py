def catalane(n):
    if n <= 1:
        return 1

    res = 0
    for i in range(n):
        res += catalane(i)*catalane(n-i-1)

    return res

for i in range(20):
    print(catalane(i), end=" ")
