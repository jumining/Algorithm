import sys
input = sys.stdin.readline

target = input().strip()
bomb = input().strip()

stack = []
for c in target:
    stack.append(c)
    if ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

print(''.join(stack)) if stack else print("FRULA")