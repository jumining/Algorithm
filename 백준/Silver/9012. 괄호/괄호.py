for _ in range(int(input())):
    stk = []
    ans = 'YES'
    for c in input():
        if c == '(':
            stk.append(c)
        else:
            if len(stk):
                stk.pop()
            else:
                ans = 'NO'
                break
    if len(stk) > 0:
        ans = 'NO'
    print(ans)