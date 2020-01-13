def maximumSum(arr,sizeOfArray):
    dp=[0]*sizeOfArray##declaring dp array
    dp[0]=arr[0]
    answer=dp[0]
    curr = arr[0]
    print(dp[0], end=" ")
    for i in range(1,sizeOfArray):
        dp[i] = max(arr[i] , arr[i]+dp[i-1])
        print(dp[i], end=" ")
        answer = max(dp[i], answer)
    print()
    return answer

arr = [5, -2, -3, 32, -5, 65]
print(maximumSum(arr, len(arr)))
