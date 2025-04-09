# time : 

DIR = [(-1,0),(0,1),(1,0),(0,-1)]

def move(y, x, dir):
    global out_sand
    
    dy, dx = DIR[dir]
    remain = board[y][x]
    val = board[y][x]

    n1dy, n1dx = DIR[(dir+1)%4]
    n2dy, n2dx = DIR[(dir-1)%4]

    def add(ny, nx, value):
        nonlocal remain
        global out_sand

        if value == 0:
            return
        if 0 <= ny < N and 0 <= nx < N:
            board[ny][nx] += value
        else:
            out_sand += value
        remain -= value

    # 1%
    tmp = int(val * 0.01)
    add(y + n1dy-dy, x + n1dx-dx, tmp)
    add(y + n2dy-dy, x + n2dx-dx, tmp)

    # 7%
    tmp = int(val * 0.07)
    add(y + n1dy, x + n1dx, tmp)
    add(y + n2dy, x + n2dx, tmp)

    # 2%
    tmp = int(val * 0.02)
    add(y + n1dy * 2, x + n1dx * 2, tmp)
    add(y + n2dy * 2, x + n2dx * 2, tmp)

    # 10%
    tmp = int(val * 0.10)
    add(y + n1dy + dy, x + n1dx + dx, tmp)
    add(y + n2dy + dy, x + n2dx + dx, tmp)

    # 5%
    tmp = int(val * 0.05)
    add(y + dy * 2, x + dx * 2, tmp)

    # remain
    ny, nx = y + dy, x + dx
    if 0 <= ny < N and 0 <= nx < N:
        board[ny][nx] += remain
    else:
        out_sand += remain
    
def moveline(i, y, x, dir_idx):
    dy, dx = DIR[dir_idx]
    for _ in range(i):
        y, x = y + dy, x + dx
        move(y, x, dir_idx)
        board[y][x] = 0      
    return y, x

# 입력
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 시뮬레이션
out_sand = 0
y, x = N//2, N//2
for i in range(1, N):
    if i%2==1:  
        # L
        y, x = moveline(i, y, x, 3)
        # D
        y, x = moveline(i, y, x, 2)
        
    else:
        # R
        y, x = moveline(i, y, x, 1)
        # U
        y, x = moveline(i, y, x, 0)

# 마지막 라인
y, x = moveline(N-1, y, x, 3)

# 출력 격자의 밖으로 나간 모래의 양
print(out_sand)