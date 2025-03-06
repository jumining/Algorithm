from collections import deque

R, C = map(int,input().split())
board = [input() for _ in range(R)]
chk = [[set() for _ in range(C)] for _ in range(R)]
ans = 0

def is_board(x, y):
  return 0 <= x < R and 0 <= y < C

dx = (0,1,-1,0)
dy = (1,0,0,-1)

q = deque()
q.append((0,0,board[0][0]))
chk[0][0].add(board[0][0])

while len(q):
  x, y, d = q.popleft()
  ans = max(ans, len(d))

  for k in range(4):
    nx, ny = x+dx[k], y+dy[k]
    if is_board(nx, ny) and board[nx][ny] not in d:
      nd = d + board[nx][ny]
      if nd not in chk[nx][ny]:
        chk[nx][ny].add(nd)
        q.append((nx,ny,nd))

print(ans)