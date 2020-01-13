def lic(arr, n):

    tail = []
    tail.append(arr[0])
    l = 1

    for i in range(1, n):
        if arr[i] > tail[-1]:
            tail.append(arr[i])
            l += 1
        else:
            c = ceil(tail, 0, l-1, arr[i])
            tail[c] = arr[i]

    return l

def ceil(tail, l, r, x):

    while r > l:
        m = l+(r-l)//2
        if tail[m] >= x:
            r = m
        else:
            l = m+1

    return r

arr = [3,10,20,4,6,7]
print(lic(arr, len(arr)))
