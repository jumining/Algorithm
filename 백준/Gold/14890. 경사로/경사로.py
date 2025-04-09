N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(line):
    used = [False] * N  # 경사로 설치 여부
    for i in range(N - 1):
        diff = line[i] - line[i + 1]

        if diff == 0:
            continue  

        elif diff == 1:  # 내리막
            for j in range(1, L + 1):
                if i + j >= N or line[i + j] != line[i + 1] or used[i + j]:
                    return False
            for j in range(1, L + 1):
                used[i + j] = True

        elif diff == -1:  # 오르막
            for j in range(L):
                if i - j < 0 or line[i - j] != line[i] or used[i - j]:
                    return False
            for j in range(L):
                used[i - j] = True

        else:  
            return False

    return True

result = 0

# 가로방향
for row in board:
    if check(row):
        result += 1

# 세로방향
for col in range(N):
    col_line = [board[row][col] for row in range(N)]
    if check(col_line):
        result += 1

print(result)
