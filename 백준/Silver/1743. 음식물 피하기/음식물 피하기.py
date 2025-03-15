from collections import deque
import sys

input = sys.stdin.readline

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M, K = map(int, input().strip().split())
board = [[0] * M for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

def is_valid(y, x):
    return 0 <= x < M and 0 <= y < N

# 큐에 초기 좌표 넣기 
# 방문 표시 후 큐에 넣기
# cnt 변수로 그룹 크기 구하기

# 큐 돌면서 그룹 크기 구하기
# 4좌표 돌면서 유효한 좌표이고 아직 방문 안했다면(1) 방문처리 후 큐에 넣기

def bfs(y, x):
    q = deque()
    q.append((y, x))
    board[y][x] = 0
    cnt = 0
    while q:
        y, x = q.popleft()
        cnt += 1
        for dy, dx in d:
            n_x, n_y = x + dx, y + dy
            if is_valid(n_y, n_x) and board[n_y][n_x] == 1:
                board[n_y][n_x] = 0
                q.append((n_y, n_x))
    return cnt

result = 1
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            result = max(result, bfs(y,x))

print(result)