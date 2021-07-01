"""http://codeforces.com/contest/242/problem/C"""

from collections import deque

KING_MOVES = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (0, -1), (-1, -1)]
max_row, max_col = float('-inf'), float('-inf')
allowed_moves = set()


def is_valid_cell(num):
    return 0 < num[0] <= max_row and 0 < num[1] <= max_col


def bfs(s, e):
    search_queue = deque()
    search_queue.append(s)
    _path = {}
    visited = set()
    visited.add(s)
    while search_queue:
        current = search_queue.popleft()
        if current == e:
            return _path
        for move in KING_MOVES:
            neighbor = current[0] + move[0], current[1] + move[1]
            if is_valid_cell(neighbor) and neighbor not in visited and neighbor in allowed_moves:
                _path[neighbor] = current
                visited.add(neighbor)
                search_queue.append(neighbor)
    return -1


if __name__ == '__main__':
    inp = list(map(int, input().split()))
    START = inp[0], inp[1]
    END = inp[2], inp[3]
    segments = int(input())
    for i in range(segments):
        r, a, b = list(map(int, input().split()))
        if r > max_row:
            max_row = r
        if b > max_col:
            max_col = b
        for j in range(a, b + 1):
            allowed_moves.add((r, j))

    path = bfs(START, END)
    if path == -1:
        print(path)
    else:
        curr = END
        movies = 0
        correct = []
        while curr != START:
            correct.append(curr)
            movies += 1
            curr = path[curr]
        print(movies)
