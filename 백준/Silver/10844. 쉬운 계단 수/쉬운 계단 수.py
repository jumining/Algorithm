dp = [[0]*10 for _ in range(101)]
for i in range(1, 10):
    dp[1][i] = 1

n = int(input())
for k in range(2, n+1):
    dp[k][0] = dp[k-1][1]
    dp[k][9] = dp[k-1][8]
    for i in range(1, 9):
        dp[k][i] = dp[k-1][i-1] + dp[k-1][i+1]

print(sum(dp[n]) % 1000000000)