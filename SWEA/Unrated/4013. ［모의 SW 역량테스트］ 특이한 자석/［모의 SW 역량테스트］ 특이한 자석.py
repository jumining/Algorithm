# import sys
# sys.stdin = open("testcase.txt", "r")

from collections import deque

def get_score(magnetic):
    a = 1 if magnetic[0][0] else 0
    b = 2 if magnetic[1][0] else 0
    c = 4 if magnetic[2][0] else 0
    d = 8 if magnetic[3][0] else 0
    return a + b + c + d

def get_rotations(idx, dir):
    rotations = [0] * 4
    rotations[idx] = dir

    for i in range(idx-1, -1, -1):
        if magnets[i][2] != magnets[i+1][6]:
            rotations[i] = -rotations[i+1]
        else:
            break

    for i in range(idx+1, 4):
        if magnets[i-1][2] != magnets[i][6]:
            rotations[i] = -rotations[i-1]
        else:
            break

    return rotations

def rotate(magnet, dir):
    if dir == 1:
        return [magnet[-1]] + magnet[:-1]
    else:
        return magnet[1:] + [magnet[0]]

T = int(input())
for t in range(T):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    cmds = [tuple(map(int, input().split())) for _ in range(K)]

    for idx, dir in cmds:
        idx -= 1
        to_rotate = get_rotations(idx, dir)
        for i in range(4):
            if to_rotate[i] != 0:
                magnets[i] = rotate(magnets[i], to_rotate[i])

    score = get_score(magnets)
    print(f"#{t+1} {score}")
