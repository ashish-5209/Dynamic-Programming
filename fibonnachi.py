def fib(n, arr):
    if arr[n] == -1:
        if n == 0 or n == 1:
            res = n
        else:
            res = fib(n-1, arr) + fib(n-2, arr)
        arr[n] = res
    return arr[n]

arr = [-1]*11
print(fib(10, arr))
print(*arr)
