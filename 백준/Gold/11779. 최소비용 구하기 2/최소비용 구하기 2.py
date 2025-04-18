import heapq
import sys
input = sys.stdin.readline

def dijkstra():
    dist = [float("inf")] * (n+1)
    dist[st] = 0
    pq = [(0, st)]
    prev = [-1] * (n+1)

    while pq:
        cur_dist, u = heapq.heappop(pq)

        if dist[u] < cur_dist: continue

        for v in range(n+1):
            if bus[u][v] == -1: continue

            for weight in bus[u][v]:
                new_weight = cur_dist + weight
                if new_weight < dist[v]:
                    dist[v] = new_weight
                    heapq.heappush(pq, (new_weight, v))
                    prev[v] = u

    path = []
    node = en
    while node != -1:
        path.append(node)
        node = prev[node]
    path.reverse()
    return dist[en], path

n = int(input())
m = int(input())
bus = [[[] for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    bus[a][b].append(c)
st, en = map(int, input().split())

min_cost, path = dijkstra()
print(min_cost)
print(len(path))
print(*path)
