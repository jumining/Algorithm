# 입력 
N, M, K = map(int, input().split())
balls = []
for _ in range(M):
    y, x, m, s, d = map(int, input().split())
    balls.append((y-1,x-1,m,s,d))

# 방향 (상수)
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# 짝홀 판단 함수
def is_all_even_or_odd(lst):
    return all(l%2==0 for l in lst) or all(l%2==1 for l in lst)

# 파이어볼 이동
def move_balls(balls):
    board = [[[] for _ in range(N)] for _ in range(N)]
    for y,x,m,s,d in balls:
        dy, dx = DIRECTIONS[d]
        ny, nx = (y+dy*s)%N, (x+dx*s)%N
        board[ny][nx].append((m,s,d))        
    return board

# 파이어볼 분할
def split_balls(board):
    balls = []
    for y in range(N):
        for x in range(N):
            cell = board[y][x]
            cnt = len(cell)
            
            if cnt == 0:
                continue
            if cnt == 1:
                balls.append((y,x,*cell[0]))
                continue

            new_m = sum(m for m,_,_ in cell) // 5
            if new_m==0:
                continue

            new_s = sum(s for _,s,_ in cell) // cnt
            directions = [d % 2 for _, _, d in cell]
            new_dirs = [0, 2, 4, 6] if all(d == directions[0] for d in directions) else [1, 3, 5, 7]
            for d in new_dirs:
                balls.append((y,x,new_m,new_s,d))

    return balls        

# 시뮬레이션
for step in range(K):
    board = move_balls(balls)
    balls = split_balls(board)

# 합 구하기
print(sum(m for _, _, m, _, _ in balls))