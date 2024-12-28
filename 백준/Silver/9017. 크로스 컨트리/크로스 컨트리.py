T = int(input())
for _ in range(T):
    n = int(input())
    inputs = list(map(int, input().split()))

    count = {}
    for i in range(n):
        if inputs[i] in count:
            count[inputs[i]] += 1
        else:
            count[inputs[i]] = 1

    dele = {}
    for k, v in count.items():
        if v < 6:
            dele[k] = 1

    team = {}
    idx = 1
    for i in range(n):
        team_id = inputs[i]
        if team_id not in dele:
            if team_id in team:
                if team[team_id][0] < 4:
                    team[team_id][0] += 1
                    team[team_id][1] += idx
                elif team[team_id][0] == 4:
                    team[team_id][0] += 1
                    team[team_id][2] = idx
            else:
                team[team_id] = [1, idx, 0] # 주자 수, 상위 4명 점수, 5번째 선수 점수
            idx += 1

    team = sorted(team.items(), key=lambda x:(x[1][1], x[1][2]))
    print(team[0][0])