def coin(arr, n, s, st):
    if s == 0:
        print(st.strip())
        return 1
    if n == 0:
        return 0
    res = coin(arr, n-1, s, st)
    if arr[n-1] <= s:
        res += coin(arr, n, s-arr[n-1], st+" "+str(arr[n-1]))
    return res

arr = [2, 5, 3, 6]
s = 10
print(coin(arr, len(arr), s, ""))
