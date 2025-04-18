import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

# x가 속한 집합의 대표를 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x]) # 경로 압축
    return parent[x]

# x와 y가 속한 집합을 하나로 합침
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root

# x의 대표(부모 노드) 저장
parent = [i for i in range(N)]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j]:
            union(i, j)

plan = [x-1 for x in map(int, input().split())]

first_root = find(plan[0])
flag = all(find(city) == first_root for city in plan)

print("YES" if flag else "NO")