import sys
input = sys.stdin.readline

def main():
    N = int(input())
    heights = list(map(int, input().split()))
    stack = []  # (높이, 인덱스)
    result = [0] * N

    for i in range(N):
        current_height = heights[i]

        while stack and stack[-1][0] < current_height:
            stack.pop()

        if stack:
            result[i] = stack[-1][1]

        stack.append((current_height, i + 1))  

    sys.stdout.write(' '.join(map(str, result)) + '\n')

main()