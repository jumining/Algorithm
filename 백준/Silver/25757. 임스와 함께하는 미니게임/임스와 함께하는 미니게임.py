N, game = input().split()
N = int(N)

my_set = set()
for _ in range(N):
    human = input()
    my_set.add(human)

num = len(my_set)


def get_result():
    if game == "Y":
        return num
    if game == "F":
        return num // 2
    if game == "O":
        return num // 3


print(get_result())
