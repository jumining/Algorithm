import sys
input = sys.stdin.readline
from math import isqrt

num = int(input().strip())
# num = 100000
dp = [0]*100001
arr = [0]*100001

j=1
for i in range(1, num+1):
    if int(i**0.5) == i**0.5:
        dp[i] = 1
        arr[j] = i
        j+=1
    else:
        dp[i] = dp[i-1] + 1
        for k in range(1, j):
            if dp[i] > dp[i-arr[k]] + 1:
                dp[i] = dp[i-arr[k]] + 1
        # print(f"# {i} : {dp[i]}, {j}")

print(dp[num])
# arr = [61495]
# for a in arr:
#     print(f"# {dp[a]}")