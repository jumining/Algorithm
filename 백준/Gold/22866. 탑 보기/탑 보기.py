import sys
input = sys.stdin.readline

N = int(input())
heights = list(map(int, input().split()))

results = [[0] * 2 for _ in range(N)]

stack = []
for i in range(N):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    if stack:
        results[i][0] = len(stack)
        results[i][1] = stack[-1] + 1
    stack.append(i)

stack = []
for i in range(N-1, -1, -1):
    while stack and heights[stack[-1]] <= heights[i]:
        stack.pop()
    if stack:
        results[i][0] += len(stack)
        if results[i][1] != 0:
            left = i - (results[i][1] - 1)
            right = stack[-1] - i
            if right < left:
                results[i][1] = stack[-1] + 1
        else:
            results[i][1] = stack[-1] + 1
    stack.append(i)

for s, n in results:
    if s==0:
        print(0)
    else:
        print(s, n)