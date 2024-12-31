def can_light_all(N, xlist, height):
    cover = 0
    for x in xlist:
        if cover < x - height:
            return False
        cover = x + height
    return cover >= N


def find_min_height(N, xlist):
    l, r = 0, N
    result = N

    while l < r:
        m = (l + r) // 2
        if can_light_all(N, xlist, m):
            result = m
            r = m
        else:
            l = m + 1

    return result


N = int(input())
M = int(input())
xlist = list(map(int, input().split()))

print(find_min_height(N, xlist))
