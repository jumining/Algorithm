# 입력 
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0
visited = [[False] * M for _ in range(N)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 유효성 검사
def in_range(y,x):
    return 0<=y<N and 0<=x<M

def dfs(y,x,depth,total):
    global max_sum

    if depth == 4:
        max_sum = max(max_sum, total)
        return
    
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if in_range(ny,nx) and not visited[ny][nx]:
            visited[ny][nx] = True
            dfs(ny,nx,depth+1,total+board[ny][nx])
            visited[ny][nx] = False

def fuck_shape(y,x):
    global max_sum
    total = board[y][x]
    values = []

    for i in range(4): 
        ny, nx = y+dy[i], x+dx[i]
        if in_range(ny, nx):
            values.append(board[ny][nx])
    if len(values) >= 3:
        values.sort(reverse=True)
        shape_sum = total + sum(values[:3])
        max_sum = max(max_sum, shape_sum)

for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(y,x,1,board[y][x])
        visited[y][x] = False
        fuck_shape(y,x)

print(max_sum)