import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
results = []

for i in range(N):
    while stack and stack[-1][0] < arr[i]:
        stack.pop()
    if stack:
        results.append(stack[-1][1])
    else:
        results.append(0)
    stack.append((arr[i], i+1))

print(' '.join(map(str, results)))