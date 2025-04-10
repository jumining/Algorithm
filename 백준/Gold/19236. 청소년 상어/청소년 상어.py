import copy

DIRS = [(-1, 0), (-1, -1), (0, -1), (1, -1),
        (1, 0), (1, 1), (0, 1), (-1, 1)]

def move_all_fish(fish_map, sy, sx):
    new_map = copy.deepcopy(fish_map)

    # 물고기 번호 → 위치 dict
    positions = {}
    for pos, (num, dir) in new_map.items():
        positions[num] = pos

    for fish_num in range(1, 17):
        if fish_num not in positions:
            continue
        y, x = positions[fish_num]
        num, dir = new_map[(y, x)]

        for i in range(8):
            nd = (dir - 1 + i) % 8
            dy, dx = DIRS[nd]
            ny, nx = y + dy, x + dx

            if not (0 <= ny < 4 and 0 <= nx < 4):
                continue
            if (ny, nx) == (sy, sx):
                continue

            # print(f"[FISH MOVE] Fish {num} from ({y},{x}) dir {dir} -> ({ny},{nx}) dir {nd+1}")
            if (ny, nx) in new_map:
                # swap
                other_num, other_dir = new_map[(ny, nx)]
                new_map[(y, x)] = (other_num, other_dir)
                new_map[(ny, nx)] = (num, nd + 1)
                positions[other_num] = (y, x)
                positions[num] = (ny, nx)
                # print(f"[SWAP] Fish {num} swaps with Fish {other_num}")
            else:
                new_map[(ny, nx)] = (num, nd + 1)
                del new_map[(y, x)]
                positions[num] = (ny, nx)

            break

    return new_map

def dfs(sy, sx, sdir, total, fish_map):
    global result
    # print(f"\n[DFS] Shark at ({sy},{sx}) dir {sdir}, total = {total}")
    result = max(result, total)
    new_map = move_all_fish(fish_map, sy, sx)

    for step in range(1, 4):
        dy, dx = DIRS[sdir - 1]
        ny, nx = sy + dy * step, sx + dx * step

        if not (0 <= ny < 4 and 0 <= nx < 4):
            break
        if (ny, nx) not in new_map:
            continue

        # 물고기 먹기
        copied_map = copy.deepcopy(new_map)
        num, ndir = copied_map[(ny, nx)]
        del copied_map[(ny, nx)]
        # print(f"[SHARK MOVE] Shark eats Fish {num} at ({ny},{nx}), new dir = {ndir}")
        dfs(ny, nx, ndir, total + num, copied_map)

# 입력 처리
fish_map = {}
for y in range(4):
    lst = list(map(int, input().split()))
    for x in range(4):
        fish_map[(y, x)] = (lst[2 * x], lst[2 * x + 1])

# 시작: (0,0) 물고기 먹기
first_num, first_dir = fish_map[(0, 0)]
del fish_map[(0, 0)]

result = 0
dfs(0, 0, first_dir, first_num, fish_map)
print(result)
