from collections import deque
import sys
input = sys.stdin.readline

def topological_sort(N, adj_list, in_degree):
    q = deque()
    result = []
    degree = in_degree[:]

    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)

    while q:
        cur = q.popleft()
        result.append(cur)

        for nxt in adj_list[cur]:
            degree[nxt] -= 1
            if degree[nxt] == 0:
                q.append(nxt)

    return result

N, M = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    in_degree[b] += 1

print(*topological_sort(N, adj_list, in_degree))