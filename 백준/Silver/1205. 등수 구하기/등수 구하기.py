def calculate_rank(scores, new_score):
    rank = 1
    for score in scores:
        if new_score < score:
            rank += 1
        else:
            break
    return rank


def determine_result(r, ns, last_score, n, p):
    if n >= p:
        if ns > last_score and r <= p:
            return r
    else:
        if r <= p:
            return r
    return -1


    # if rank > p:
    #     print("*1")
    #     return -1
    # if rank == p:
    #     if new_score > last_score:
    #         print("*2")
    #         return rank
    #     print("*3")
    #     return -1
    # if new_score == last_score and len(scores) == p:
    #     print("*4")
    #     return -1
    # print("*5")
    # return rank


N, new_score, P = map(int, input().split())

if N == 0:  # 점수 목록이 비어 있는 경우
    print(1 if P > 0 else -1)
else:
    scores = list(map(int, input().split()))
    rank = calculate_rank(scores, new_score)
    print(determine_result(rank, new_score, scores[-1], N, P))
