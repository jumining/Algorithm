import sys
input = sys.stdin.readline

N = int(input())
heights = [int(input()) for _ in range(N)]

stack = []
visible_count = 0

for h in heights:
    while stack and h >= stack[-1]:
        stack.pop()
    visible_count += len(stack)
    stack.append(h)

print(visible_count)