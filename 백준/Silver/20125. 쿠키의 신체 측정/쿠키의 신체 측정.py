N = int(input())
arr = [list(input()) for _ in range(N)]


def get_length(x, y, dx, dy):
    length = 0
    while 0 <= x + dx * (length + 1) < N and 0 <= y + dy * (length + 1) < N:
        if arr[x + dx * (length + 1)][y + dy * (length + 1)] != "*":
            break
        length += 1
    return length


def find_head_position():
    for x in range(N):
        for y in range(N):
            if arr[x][y] == "*":
                return x, y


head_x, head_y = find_head_position()
heart_x, heart_y = head_x + 1, head_y
print(heart_x + 1, heart_y + 1)

left_arm_length = get_length(heart_x, heart_y, 0, -1)
right_arm_length = get_length(heart_x, heart_y, 0, 1)
waist_length = get_length(heart_x, heart_y, 1, 0)

waist_end_x = heart_x + waist_length
waist_end_y = heart_y

left_leg_length = get_length(waist_end_x, waist_end_y - 1, 1, 0)
right_leg_length = get_length(waist_end_x, waist_end_y + 1, 1, 0)

print(left_arm_length, right_arm_length, waist_length, left_leg_length, right_leg_length)
