import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[False] * (N+1) for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, input().split())
  adj[u][v] = True
  adj[v][u] = True
ans = 0
chk = [False] * (N+1)

def dfs(i):
  for j in range(1+N):
    if adj[i][j] and not chk[j]: 
      chk[j] = True
      dfs(j)

for i in range(1, N+1):
  if not chk[i]:
    ans += 1
    chk[i] = True
    dfs(i)

print(ans)