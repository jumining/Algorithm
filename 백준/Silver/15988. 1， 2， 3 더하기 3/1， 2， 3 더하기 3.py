import sys
input = sys.stdin.readline

t = int(input().strip())
dp = [1] * 1000001
dp[2] = 2
for i in range(3, 1000001):
    dp[i] = dp[i-3] % 1000000009 + dp[i-2] % 1000000009 + dp[i-1] % 1000000009

for _ in range(t):
    n = int(input().strip())
    print(dp[n]%1000000009)