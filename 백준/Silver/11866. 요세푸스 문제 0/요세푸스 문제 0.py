import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
pt = 0
ans = []
for _ in range(N):
    pt += K-1
    pt %= len(arr)
    ans.append(arr.pop(pt))

print(f"<{', '.join(map(str,ans))}>")