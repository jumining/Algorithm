from collections import deque

# 입력 
N, M, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 위, 오른, 아래, 왼
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] 
dice = [1,4,3,5,6,2]
global_idx = 1 # 초기 방향 동쪽

def change_dir_idx(A, B):
    global dir_idx
    if A > B:
        # 오른쪽으로 회전
        dir_idx = (dir_idx + 1) % 4
    elif A < B:
        # 왼쪽으로 회전
        dir_idx = (dir_idx - 1) % 4
    # print(f"{'시계방향 회전' if A > B else '시계반대방향 회전'} -> {get_directions_korean(dir_idx)}쪽으로")

def rotate(dir_idx):
    a,b,c,d,e,f = dice

    if dir_idx == 1: # 오른쪽
        dice[0], dice[1], dice[2], dice[4] = b, e, a, c
    elif dir_idx == 3: # 왼쪽
        dice[0], dice[1], dice[2], dice[4] = c, a, e, b
    elif dir_idx == 0: # 위쪽
        dice[0], dice[3], dice[4], dice[5] = d, e, f, a
    elif dir_idx == 2: #아래쪽
        dice[0], dice[3], dice[4], dice[5] = f, a, d, e

def dfs(y, x, b):
    global cnt
    visited[y][x] = True
    cnt += 1
    for dx, dy in dir: 
        ny, nx = y + dy,  x + dx
        if in_range(ny, nx) and not visited[ny][nx] and board[ny][nx] == b:
            dfs(ny, nx, b)

def in_range(y, x):
    return 0<=y<N and 0<=x<M

# 디버깅용
def get_directions_korean(dir_idx):
    return { 
        0: '북',
        1: '동',
        2: '남',
        3: '서'
    }.get(dir_idx)

total = 0
dir_idx = 1
y, x = 0, 0
for _ in range(K):
    dy, dx = dir[dir_idx]

    # dfs 초기화
    visited = [[False] * M for _ in range(N)]
    cnt = 0

    # 만약, 이동 방향에 칸이 없다면, 이동 방향을 반대로 한다.
    if not in_range(y + dy, x + dx):
        dir_idx = (dir_idx + 2) % 4

    # 이동 방향으로 한 칸 굴러간다.
    dy, dx = dir[dir_idx]
    rotate(dir_idx)
    y += dy
    x += dx
    # print(f"\n{get_directions_korean(dir_idx)}쪽으로 굴러감 -> {y+1, x+1}")
    # print(f"  🎲 주사위: {dice[5], dice[1], dice[0], dice[2], dice[3], dice[4]}")
    
    # dfs로 이동 가능한 칸의 수를 구해서 점수 구하기
    dfs(y, x, board[y][x])
    # print(f"  B가 {board[y][x]}인 칸 수 : {cnt}")
    
    A = cnt * board[y][x]
    # print(f"  💯 점수: {A}")

    # 점수 합하기
    total += A

    # 값 비교해서 이동 방향을 결정한다.
    change_dir_idx(dice[4], board[y][x])

print(total)