import sys
input = sys.stdin.readline

from collections import deque

n = int(input().strip())
k = int(input().strip())
computers = [[] for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    computers[a].append(b)
    computers[b].append(a)

def bfs(start):
    visited = [False] * (n+1)
    q = deque([start])
    visited[start] = True
    cnt = 0

    while q:
        cur_computer = q.popleft()
        for next_computer in computers[cur_computer]:
            if not visited[next_computer]:
                q.append(next_computer)
                visited[next_computer] = True
                cnt += 1
    
    return cnt

print(bfs(1))