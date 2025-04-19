import sys
input = sys.stdin.readline

target = input().strip()
bomb = input().strip()

stack = []
for c in target:
    stack.append(c)
    if c == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
        del stack[-len(bomb):]

print(''.join(stack)) if stack else print("FRULA")