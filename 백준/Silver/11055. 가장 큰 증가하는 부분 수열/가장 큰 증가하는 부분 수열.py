import sys
input = sys.stdin.readline
num = int(input().strip())

arr = list(map(int, input().split()))
dp = arr[:]

for i in range(num):
    for j in range(i-1, -1, -1):
        if arr[j] < arr[i]:
            # print(f"    {i}: {dp[i]}, {arr[i]+dp[j]}")
            dp[i] = max(dp[i], arr[i]+dp[j])
            
print(max(dp))         