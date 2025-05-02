dp = [1] * 101
dp[4] = 2
dp[5] = 2
for i in range(6, 101):
    dp[i] = dp[i-1] + dp[i-5]

T = int(input())
for i in range(T):
    n = int(input())
    print(dp[n])