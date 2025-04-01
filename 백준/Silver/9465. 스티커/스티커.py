import sys
input = sys.stdin.readline

for _ in range (int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    if n==1:
        print(max(arr[0][0], arr[1][0]))
        continue
    
    dp = [[0] * 2 for _ in range(n)]
    dp[0][0] = arr[0][0]
    dp[0][1] = arr[1][0]
    dp[1][0] = dp[0][1] + arr[0][1]
    dp[1][1] = dp[0][0] + arr[1][1]

    for i in range(2, n):
        dp[i][0] = max(dp[i-1][1] + arr[0][i], dp[i-2][1] + arr[0][i])
        dp[i][1] = max(dp[i-1][0] + arr[1][i], dp[i-2][0] + arr[1][i])

    print(max(dp[n-1]))
