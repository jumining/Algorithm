import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

stack = []
results = [-1] * N

for i in range(N-1, -1, -1):
    while stack and stack[-1] <= nums[i]:
        stack.pop()
    if stack:
        results[i] = stack[-1]
    stack.append(nums[i])

print(*results)