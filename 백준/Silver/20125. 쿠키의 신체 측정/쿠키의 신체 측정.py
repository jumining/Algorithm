N = int(input())
arr = [list(input()) for _ in range(N)]


def get_headx_heady():
    for x in range(N):
        for y in range(N):
            if arr[x][y] == "*":
                return x, y


def get_left_arm_length():
    i = 0
    while hy - 1 - i >= 0 and arr[hx][hy - 1 - i] == "*":
        i += 1
    return i


def get_right_arm_length():
    i = 0
    while hy + 1 + i <= N - 1 and arr[hx][hy + 1 + i] == "*":
        i += 1
    return i


def get_waist():
    i = 0
    while hx + 1 + i <= N - 1 and arr[hx + 1 + i][hy] == "*":
        i += 1
    return i, hx + i, hy


def get_left_leg_length():
    i = 0
    while wx + 1 + i <= N - 1 and arr[wx + 1 + i][wy - 1] == "*":
        i += 1
    return i


def get_right_leg_length():
    i = 0
    while wx + 1 + i <= N - 1 and arr[wx + 1 + i][wy + 1] == "*":
        i += 1
    return i


head_x, head_y = get_headx_heady()
hx, hy = head_x + 1, head_y
print(hx + 1, hy + 1)
length_left_arm = get_left_arm_length()
length_right_arm = get_right_arm_length()
length_waist, wx, wy = get_waist()
length_left_leg = get_left_leg_length()
length_right_leg = get_right_leg_length()
print(length_left_arm, length_right_arm, length_waist, length_left_leg, length_right_leg)
