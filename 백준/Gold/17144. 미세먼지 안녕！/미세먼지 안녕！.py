# 2h 15m 소요

DIR = [(-1,0),(0,1),(1,0),(0,-1)]

def dust_spread():
    global R, C

    tmp = [[[0, 0] for _ in range(C)] for _ in range(R)]
    for y in range(R):
        for x in range(C):
            cnt = 0
            reassign = []
            if arr[y][x] != 0 and arr[y][x] != -1:
                for dy, dx in DIR:
                    ny, nx = y+dy, x+dx
                    if 0<=ny<R and 0<=nx<C and arr[ny][nx] != -1:
                        cnt += 1
                        reassign.append((ny,nx))
                
                new_val = arr[y][x] // 5
                for ry, rx in reassign:
                    tmp[ry][rx][1] += new_val
                remain_val = arr[y][x] - new_val * cnt
                tmp[y][x][0] = remain_val
    
    # arr에 적용
    for y in range(R):
        for x in range(C):
            if tmp[y][x] != [0,0]:
                arr[y][x] = tmp[y][x][0] + tmp[y][x][1]

def air_clean(a, b):
    global R, C

    # 반시계 순환 
    for i in range(a-1, 0, -1): 
        arr[i][0] = arr[i-1][0]
    for i in range(C-1):
        arr[0][i] = arr[0][i+1]
    for i in range(a):
        arr[i][C-1] = arr[i+1][C-1]
    for i in range(C-1, 1, -1):
        arr[a][i] = arr[a][i-1]
    arr[a][1] = 0

    # 시계 순환
    for i in range(b+1, R-1):
        arr[i][0] = arr[i+1][0]
    for i in range(C-1):
        arr[R-1][i] = arr[R-1][i+1]
    for i in range(R-1, b, -1):
        arr[i][C-1] = arr[i-1][C-1]
    for i in range(C-1, 1, -1):
        arr[b][i] = arr[b][i-1]
    arr[b][1] = 0   


# 입력
R, C, T = map(int, input().split())

arr = []
a, b = -1, -1
for y in range(R):
    lst = list(map(int, input().split()))
    arr.append(lst)
    if lst[0] == -1 and a == -1:
        a, b = y, y+1

for i in range(T):
    dust_spread()
    air_clean(a, b)

print(sum(x for row in arr for x in row if x != -1))