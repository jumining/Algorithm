import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
t = arr[0]
cnt = 1

for i in range(1, len(arr)):
    if arr[i] >= t + L:
        cnt += 1
        t = arr[i]

print(cnt)