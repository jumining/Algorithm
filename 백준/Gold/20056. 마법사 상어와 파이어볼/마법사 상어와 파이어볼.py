# 입력 
N, M, K = map(int, input().split())
balls = []
for _ in range(M):
    y, x, m, s, d = map(int, input().split())
    balls.append((y-1,x-1,m,s,d))

# 8가지 방향
dir = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# 짝홀 판단 함수
def is_all_even_or_odd(lst):
    return all(l%2==0 for l in lst) or all(l%2==1 for l in lst)

# 각 볼 방향대로 속력만큼 이동
def move_balls(balls):
    board = [[[] for _ in range(N)] for _ in range(N)]
    for y,x,m,s,d in balls:
        dy, dx = dir[d]
        ny, nx = (y+dy*s)%N, (x+dx*s)%N
        board[ny][nx].append((m,s,d))        
    return board

def split_balls(board):
    balls = []
    for y in range(N):
        for x in range(N):
            cnt_ball = len(board[y][x])
            if cnt_ball >= 2:
                new_s = sum(s for _,s,_ in board[y][x]) // cnt_ball
                new_m = sum(m for m,_,_ in board[y][x]) // 5
                if new_m==0:
                    continue

                arr_d = [d for _,_,d in board[y][x]]
                new_dirs = [0,2,4,6] if is_all_even_or_odd(arr_d) else [1,3,5,7]
                
                for idx in new_dirs:
                    dy, dx = dir[idx]
                    balls.append((y,x,new_m,new_s,idx))

            elif cnt_ball == 1:
                m,s,d=board[y][x][0]
                balls.append((y,x,m,s,d))
    return balls        

# K번 파이어볼 이동
for step in range(K):
    board = move_balls(balls)
    balls = split_balls(board)

# 합 구하기
print(sum(m for _, _, m, _, _ in balls))