import sys
input = sys.stdin.readline

n = int(input().strip())
cards = list(map(int, input().split()))
cards = [0] + cards

dp = [0] * (n + 1)
dp[1] = cards[1]
for i in range(2, n+1):
    max_value = 0
    for k in range(1, i+1):
        tmp = dp[i-k] + cards[k]
        max_value = max(max_value, tmp)
    dp[i] = max_value

print(dp[n])