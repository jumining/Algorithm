# 11:53 - 12:00, 13:13-

DIAGONAL = [(-1,-1), (-1,1), (1,1), (1,-1)]
DIR = [(),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

# 모든 구름 이동
def move(d,s):
    dy, dx = DIR[d]
    new_clouds = []
    for cy, cx in clouds:
        ny, nx = (cy+dy*s)%N, (cx+dx*s)%N
        new_clouds.append((ny,nx))
    return new_clouds

def watercopy(y, x):
    # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 
    # (r,c)에 있는 바구니의 물 양 증가
    # 행, 열 연결 가정 X
    cnt = 0
    tmp = []
    for dy, dx in DIAGONAL:
        ny, nx = y+dy, x+dx
        if 0<=ny<N and 0<=nx<N and board[ny][nx] != 0:
            cnt += 1
            tmp.append((ny,nx))


    board[y][x] += cnt

# 입력
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cmd = [list(map(int, input().split())) for _ in range(M)]

# 시뮬레이션
clouds = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
for step, (d, s) in enumerate(cmd,1):
    increased = []
    isUsed = [[False] * N for _ in range(N)]

    # 모든 구름이 d방향으로 s칸 이동
    clouds = move(d,s)

    # 모든 구름 있는 칸의 물의 양 += 1
    for y,x in clouds:
        board[y][x] += 1
        increased.append((y,x))
        isUsed[y][x] = True

    # 모든 구름 사라짐
    clouds = []

    # 물복사 마법
    for y,x in increased:
        watercopy(y,x)
    
    # 물의 양 2 이상이고 이전에 구름 안생겼으면 
    # 물의 양 2 줄어들고 구름 생김
    for y in range(N):
        for x in range(N):
            if board[y][x] >= 2 and not isUsed[y][x]:
                board[y][x] -= 2
                clouds.append((y,x))

print(sum(sum(row) for row in board))