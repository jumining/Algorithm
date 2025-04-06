from collections import deque

# 입력 
N, M = map(int, input().split())
y, x, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)] # 0은 청소해야할 칸, 1은 벽

# 방향 (상수)
DIRECTIONS = [(-1,0),(0,1),(1,0),(0,-1)]

def is_in_range_and_not_wall(y, x):
    return 0<=y<N and 0<=x<M and room[y][x] != 1

def is_4ways_clean():
    for dy, dx in DIRECTIONS:
        ny, nx = y + dy, x + dx  
        if is_in_range_and_not_wall(ny, nx) and not cleaned[ny][nx]:
            return False
    return True

cleaned = [[False]*M for _ in range(N)]

while True:
    cleaned[y][x] = True

    # all done 청소 - 후진, 벽이면 stop
    if is_4ways_clean():
        dy, dx = DIRECTIONS[d]
        ny, nx = y - dy, x - dx
        if is_in_range_and_not_wall(ny, nx):
            y, x = ny, nx
        else:
            break

    # should 청소 - 방향 업데이트, 전진필요하면 전진
    else:
        d = (d-1) % 4 
        dy, dx = DIRECTIONS[d]
        ny, nx = y + dy, x + dx
        if is_in_range_and_not_wall(ny, nx) and not cleaned[ny][nx]:
            y, x = ny, nx

print(sum(cell for row in cleaned for cell in row))