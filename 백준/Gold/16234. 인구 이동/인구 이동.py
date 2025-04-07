from collections import deque

DIRECTIONS = [(-1,0), (0, 1), (1,0), (0,-1)]

def seek_union(y, x):
    global R, M

    q = deque()
    q.append((y,x))
    visited[y][x] = True    
    
    union = [(y,x)]
    total = peoples[y][x]
    
    while q:
        y, x = q.popleft()
        for dy, dx in DIRECTIONS:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if R <= abs(peoples[y][x]-peoples[ny][nx]) <= M:
                    visited[ny][nx] = True
                    q.append((ny,nx))
                    union.append((ny, nx))
                    total += peoples[ny][nx]
    return union, total

def redistribute(union, total):
    nv = total // len(union)
    for y,x in union:
        peoples[y][x] = nv

# 입력 처리
N, R, M = map(int, input().split())
peoples = [list(map(int, input().split())) for _ in range(N)]

day = 0
while True:
    moved = False
    visited = [[False]*N for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                union, total = seek_union(y,x)
                if len(union) >= 2:
                    moved = True
                    redistribute(union, total)   
    if not moved:
        break
    day += 1                      

print(day)
