def lis(arr, n):

    l = [1]*n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                l[i] = max(l[i], l[j]+1)

    return max(l)

arr = [10,5,18,7,2,9]
print(lis(arr, len(arr)))
