from collections import deque

N, M = map(int, input().split())
adj = []
board = [[1] * (M+1) for _ in range(N+1)]

for _ in range(N):
  adj.append(list(map(int, input())))

dy = (0, 1, 0 ,-1)
dx = (1, 0, -1 ,0)
chk = [[False] * (M+1) for _ in range(N+1)]

def is_valid(x, y):
  return 0 <= x < N and 0 <= y < M

def bfs(x, y):
  q = deque()
  chk[x][y] = True
  q.append((x, y))

  while len(q):
    x, y = q.popleft()
    if x==N-1 and y==M-1:
      return board[x][y]

    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]
      if is_valid(nx, ny) and adj[nx][ny] == 1 and not chk[nx][ny]:
        board[nx][ny] = board[x][y] + 1
        chk[nx][ny] = True
        q.append((nx, ny))

print(bfs(0,0))