from collections import deque

# 입력 
N, M, y, x, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
cmds = list(map(int, input().split()))

# 오른, 왼, 위, 아래
dir = [(),(0, 1), (0, -1), (-1, 0), (1, 0)] 
dice = [0,0,0,0,0,0]

def rotate(cmd):
    a,b,c,d,e,f = dice
    if cmd == 1:
        dice[0], dice[1], dice[2], dice[4] = b, e, a, c
    elif cmd == 2:
        dice[0], dice[1], dice[2], dice[4] = c, a, e, b
    elif cmd == 3:
        dice[0], dice[3], dice[4], dice[5] = d, e, f, a
    elif cmd == 4:
        dice[0], dice[3], dice[4], dice[5] = f, a, d, e


for cmd in cmds:
    # 지도 범위 체크
    dy, dx = dir[cmd]
    if y+dy == N or x+dx == M or y+dy == -1 or x+dx == -1:
        continue

    # 주사위 돌리기
    rotate(cmd)
    y += dy
    x += dx
    
    # 새 칸 값 0일 때 - 칸에 바닥면 수 할당
    if board[y][x] == 0:
        board[y][x] = dice[4]
    # 새 칸 값 1,2,3 ...일 때 - 주사위 바닥면에 칸 수 할당, 칸은 0으로 변경
    else:
        dice[4] = board[y][x]
        board[y][x] = 0

    print(dice[0])