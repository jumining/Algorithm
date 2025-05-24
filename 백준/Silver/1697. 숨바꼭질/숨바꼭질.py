from collections import deque

def bfs(v):
  q = deque([v])
  while q:
    v = q.popleft()
    if v==k:
      return arr[v]
    for nv in (v-1, v+1, v*2):
      if 0<=nv<max and not arr[nv]:
        arr[nv] = arr[v]+1
        q.append(nv)


max = 100001
n,k = map(int, input().split())
arr = [0]*max
print(bfs(n))