def catalane(n):
    if n <= 1:
        return 1

    arr = [0 for i in range(n+1)]
    arr[0] = 1
    arr[1] = 1

    for i in range(2, n+1):
        arr[i] = 0
        for j in range(i):
            arr[i] = arr[i] + arr[j]*arr[i-j-1]

    return arr[n]

for i in range(15):
    print(catalane(i), end=" ")
