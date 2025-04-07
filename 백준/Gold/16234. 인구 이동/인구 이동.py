from collections import deque

DIRECTIONS = [(-1,0), (0, 1), (1,0), (0,-1)]

def seek_union(y, x):
    global R, M

    q = deque()
    q.append((y,x))
    visited[y][x] = True    
    
    union = []
    us = []
    sum = 0
    
    while q:
        y, x = q.popleft()
        union.append((y, x))
        sum += peoples[y][x]
        us.append(peoples[y][x])
        for dy, dx in DIRECTIONS:
            ny, nx = y+dy, x+dx
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                if R <= abs(peoples[y][x]-peoples[ny][nx]) <= M:
                    q.append((ny,nx))
                    visited[ny][nx] = True
    return union, sum, us

def redistribute(union, union_sum):
    nv = union_sum // len(union)
    for y,x in union:
        peoples[y][x] = nv

N, R, M = map(int, input().split())
peoples = [list(map(int, input().split())) for _ in range(N)]

day = 0
moved = True
while moved:
    moved = False
    visited = [[False]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if not visited[y][x]:
                union, sum, us = seek_union(y,x)
                if len(union) >= 2:
                    moved = True
                    redistribute(union, sum)   
    if moved:
        day += 1                      

print(day)
