from collections import deque

BOARD_SIZE = 100

N, M = map(int, input().split())
move = [i for i in range(BOARD_SIZE + 1)]

for i in range(N+M):
    a, b = map(int, input().split())
    move[a] = b

def bfs():
    visited = [False] * (BOARD_SIZE + 1)
    q = deque([(1, 0)])
    visited[1] = True

    while q:
        cur_pos, cur_cnt = q.popleft()

        if cur_pos == BOARD_SIZE:
            return cur_cnt

        for i in range(1, 7):
            next_pos = cur_pos + i
            if next_pos <= BOARD_SIZE and not visited[move[next_pos]]:
                visited[move[next_pos]] = True
                q.append((move[next_pos], cur_cnt + 1))

print(bfs())