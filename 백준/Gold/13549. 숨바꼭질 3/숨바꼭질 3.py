from collections import deque
N, K = map(int, input().split())

def bfs(n, t):
    q = deque()
    q.append((n,t))
    visited = [False] * 100001
    while q:
        n, t = q.popleft()
        visited[n] = True
        
        if n==K:
            return t
        
        moves = [2*n, n-1, n+1]
        for nv in moves:
            if 0<=nv<=100000 and not visited[nv]:
                if nv==2*n:
                    q.appendleft((nv, t))
                else:
                    q.append((nv, t+1))
                visited[nv] = True

t = bfs(N, 0)
print(t)