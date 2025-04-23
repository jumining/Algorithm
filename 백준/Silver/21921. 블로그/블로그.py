from collections import defaultdict

N, X = map(int, input().split())
visitors = list(map(int, input().split()))

max_val = sum(visitors[:X])
count = defaultdict(int)
count[max_val] = 1

cur_sum = max_val
for i in range(X, N):
    cur_sum += visitors[i] - visitors[i - X]
    max_val = max(max_val, cur_sum)
    count[cur_sum] += 1

if max_val == 0:
    print("SAD")
else:
    print(max_val)
    print(count[max_val])