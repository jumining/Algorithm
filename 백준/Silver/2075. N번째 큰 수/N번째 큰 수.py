import heapq

hq = []
N = int(input())
for _ in range(N):
    for elem in list(map(int, input().split())):
        heapq.heappush(hq, elem)
        if len(hq) > N:
            heapq.heappop(hq)

print(heapq.heappop(hq))