from collections import deque

# 입력 
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 방향: 북(0), 동(1), 남(2), 서(3)
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 주사위: [t, r, b, l, f, ba]
dice = [1,3,6,4,5,2]

# 점수 캐시
score_cache = [[0] * M for _ in range(N)]

# 범위 유효성
def in_range(y, x):
    return 0<=y<N and 0<=x<M

# 조건 따라 방향 바꾸기
def change_dir(A, B, d):
    if A > B:
        return (d + 1) % 4  # 시계
    elif A < B:
        return (d + 3) % 4  # 반시계
    return d

# 주사위 회전 로직
def rotate(d):
    t, r, b, l, f, ba = dice
    if d == 0:  # 북
        dice[:] = [f, r, ba, l, b, t]
    elif d == 1:  # 동
        dice[:] = [l, t, r, b, f, ba]
    elif d == 2:  # 남
        dice[:] = [ba, r, f, l, t, b]
    elif d == 3:  # 서
        dice[:] = [r, b, l, t, f, ba]

# 점수 구하기
def get_score(y,x):
    if score_cache[y][x]:
        return score_cache[y][x]
    
    val = board[y][x]
    visited = [[False]*M for _ in range(N)]
    visited[y][x] = True
    q = deque([(y,x)])
    cnt = 1

    while q:
        cy, cx = q.popleft()
        for dy, dx in dir:
            ny, nx = cy + dy, cx + dx
            if in_range(ny, nx) and not visited[ny][nx] and board[ny][nx] == val:
                visited[ny][nx] = True
                q.append((ny,nx))
                cnt += 1
    
    score = cnt * val
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                score_cache[i][j] = score
    return score

# 시작 사전 정보
y, x, dir_idx = 0, 0, 1 
total = 0

for _ in range(K):
    dy, dx = dir[dir_idx]

    # 이동 방향에 칸이 없다면, 이동 방향을 반대로
    if not in_range(y + dy, x + dx):
        dir_idx = (dir_idx + 2) % 4
        dy, dx = dir[dir_idx]

    # 이동 방향으로 한 칸 굴러가기
    rotate(dir_idx)
    y += dy
    x += dx
    # print(f"\n🌀 회전 후 위치: ({y+1}, {x+1}) | 방향: {['북','동','남','서'][dir_idx]}")
    # print(f"🎲 주사위 상태: {dice}")

    # 점수 구하기 - bfs 이용 
    s = get_score(y,x)
    total += s # 같은 칸 개수 * 값
    # print(f"💯 점수: {s} (B: {board[y][x]})")

    # 값 비교해서 이동 방향을 결정하기
    # prev_dir = dir_idx
    dir_idx = change_dir(dice[2], board[y][x], dir_idx)
    # print(f"➡️ 방향 전환: A(바닥): {dice[2]}, B(지도): {board[y][x]} | {['북','동','남','서'][prev_dir]} → {['북','동','남','서'][dir_idx]}")

print(total)