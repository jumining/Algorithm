from collections import deque

N, M = map(int, input().split())
ladders = [0] * 101
snakes = [0] * 101
for i in range(N):
    a, b = map(int, input().split())
    ladders[a] = b
for i in range(M):
    a, b = map(int, input().split())
    snakes[a] = b

def bfs(cur_pos, cur_cnt):
    visited = [False] * 101
    q = deque([(cur_pos, cur_cnt)])
    visited[cur_pos] = True
    while q:
        cur_pos, cur_cnt = q.popleft()

        if ladders[cur_pos]:
            cur_pos = ladders[cur_pos]
        if snakes[cur_pos]:
            cur_pos = snakes[cur_pos]

        if cur_pos == 100:
            return cur_cnt

        for i in range(1, 7):
            if cur_pos + i <= 100 and not visited[cur_pos + i]:
                q.append((cur_pos + i, cur_cnt + 1))
                visited[cur_pos + i] = True
                
print(bfs(1, 0))