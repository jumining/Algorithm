import sys
input = sys.stdin.readline
# sys.stdin = open('testcase.txt', 'r')

stack=[]
for i in range(int(input().strip())):
    cmd = input().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif cmd[0] == 'top':
        print(stack[-1] if len(stack) > 0 else -1)