from collections import deque

S = input()
T = input()

def bfs(start):
    q = deque([start])

    while q:
        cur = q.popleft()

        if cur == S:
            print(1)
            return

        if len(cur) < len(S):
            continue

        if cur[-1] == 'A':
            q.append((cur[:-1]))

        if cur[0] == 'B':
            q.append(cur[1:][::-1])
    print(0)

bfs(T)