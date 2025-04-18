from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
city = [list(map(int, input().split())) for _ in range(N)]
plan = [x-1 for x in map(int, input().split())]

def bfs(start, end):
    visited = [False] * N
    q = deque([start])
    visited[start] = True

    while q:
        cur = q.popleft()
        if cur == end:
            return True

        for i in range(N):
            if not visited[i] and city[cur][i]:
                visited[i] = True
                q.append(i)

    return False

flag = True
for i in range(len(plan)-1):
    if not bfs(plan[i], plan[i+1]):
        flag = False

print("YES") if flag else print("NO")