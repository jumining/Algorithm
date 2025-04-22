def count_moves(balls, color):
    left = 0
    while left < len(balls) and balls[left] == color:
        left += 1
    right = len(balls) - 1
    while right >= 0 and balls[right] == color:
        right -= 1
    left_move = balls[left:].count(color)
    right_move = balls[:right+1].count(color)
    
    return min(left_move, right_move)

n = int(input())
balls = input().strip()

result = min(count_moves(balls, 'R'), count_moves(balls, 'B'))
print(result)
