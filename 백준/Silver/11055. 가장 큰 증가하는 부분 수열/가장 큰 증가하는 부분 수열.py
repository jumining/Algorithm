import sys
input = sys.stdin.readline
num = int(input().strip())

arr = list(map(int, input().split()))
dp = [0] * num
dp[0] = arr[0]

for i in range(1, num):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += arr[i]
            
print(max(dp))