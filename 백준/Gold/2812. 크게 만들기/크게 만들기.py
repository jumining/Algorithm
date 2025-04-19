# 자기보다 작은 앞 숫자들을 제거 -> K번

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = input().strip()

stack = []
for i in range(N):
    while stack and K > 0 and stack[-1] < num[i]:
        stack.pop()
        K -= 1
    stack.append(num[i])

if K > 0:
    stack = stack[:-K]

print(''.join(stack))