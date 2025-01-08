import sys

N, M = map(int, sys.stdin.readline().split())
words = {}

for _ in range(N):
  word = sys.stdin.readline().strip()
  if len(word) >= M:
    words[word] = words.get(word, 0) + 1
  
words = sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for w, _ in words:
  print(w)