from collections import deque
import sys
input = sys.stdin.readline

def get_new_str(cmds, ori_nums):
    nums = deque(ori_nums)
    reverse_flag = False
    for cmd in cmds:
        if cmd == 'R':
            reverse_flag = not reverse_flag
        else:
            if not nums:
                return "error"
            if reverse_flag:
                nums.pop()
            else:
                nums.popleft()

    if reverse_flag:
        nums.reverse()
    return '['+','.join(map(str,nums))+']'

T = int(input().strip())
for _ in range(T):
    cmds = input().strip()
    n = int(input().strip())
    s = input().strip().strip('[]')
    nums = [int(x) for x in s.split(',')] if s else []

    print(get_new_str(cmds, nums))
