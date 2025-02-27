import sys
input = sys.stdin.readline

N = int(input())
ans = 1
board = [list(input()) for _ in range(N)]

def search():
    global ans
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j-1] == board[i][j]: 
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1  

    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i-1][j] == board[i][j]: 
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 1             

    
for i in range(N):
    for j in range(N):
        if j < N-1:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            search()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i < N-1:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            search()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)