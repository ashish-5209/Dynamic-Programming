import sys
def getMinCoin(arr, n , val):
    if val == 0:
        return 0
    res = sys.maxsize

    for i in range(n):
        if arr[i] <= val:
            sub_res = getMinCoin(arr, n, val-arr[i])
            if sub_res != sys.maxsize:
                res = min(res, sub_res+1)

    return res

arr = [10, 25, 5]
val = 30
print(getMinCoin(arr, len(arr), val))
