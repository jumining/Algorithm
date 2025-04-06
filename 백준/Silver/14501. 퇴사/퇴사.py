N = int(input())
t = [0] * N
p = [0] * N
for i in range(N):
    t[i], p[i] = map(int, input().split())

dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    if i+t[i] <= N:
        dp[i] = max(p[i] + dp[i+t[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]
        
print(dp[0])