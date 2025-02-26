import sys
input = sys.stdin.readline

books = dict()
for _ in range(int(input())):
    name = input()
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

sorted_books = sorted(books.items(), key=lambda x: (-x[1], x[0]))

print(sorted_books[0][0])