import sys
input = sys.stdin.readline

arr = set()
for _ in range(int(input())):
    name, el = map(str, input().split())
    if el == 'enter':
        arr.add(name)
    else:
        arr.remove(name)

sorted_arr = sorted(arr, reverse=True)
print('\n'.join(sorted_arr))
