for _ in range(int(input())):
    pwd = []
    tmp = []
    for c in input():
        if c == '<':
            if len(pwd):
                tmp.append(pwd.pop())
        elif c == '>':
            if len(tmp):
                pwd.append(tmp.pop())
        elif c == '-':
            if len(pwd):
                pwd.pop()
        else:
            pwd.append(c)

    print(''.join(pwd),''.join(tmp[::-1]),sep='')